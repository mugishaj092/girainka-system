from django.db import models
import uuid

class Source(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    province = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    cell = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.village}, {self.cell}"
    class Meta:
        db_table = "sources"


class Cow(models.Model):
    HEALTHY = 'healthy'
    SICK = 'sick'
    DEAD = 'dead'
    STATUS_CHOICES = [
        (HEALTHY, 'Healthy'),
        (SICK, 'Sick'),
        (DEAD, 'Dead'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    owner = models.OneToOneField(
        'members.User',
        on_delete=models.CASCADE,
        related_name='owned_cow',
        null=True,
        blank=True
    )
    source = models.ForeignKey(
        Source,
        on_delete=models.CASCADE,
        related_name='cows',
        null=True,
        blank=True
    )
    giver_Id = models.OneToOneField(
        'members.User',
        on_delete=models.CASCADE,
        related_name='given_cow',
        null=True,
        blank=True
    )
    giver_away_Id = models.OneToOneField(
        'members.User',
        on_delete=models.CASCADE,
        related_name='cow_given_away',
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=HEALTHY
    )
    reason = models.TextField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "cows"