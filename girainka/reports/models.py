from django.db import models
import uuid

class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=False)
    message = models.TextField()
    user_id = models.OneToOneField(
        'members.User',
        on_delete=models.CASCADE,
        related_name='report_user',
        null=True,
        blank=True,
        default=uuid.uuid4
    )
    cow_id = models.OneToOneField(
        'cows.Cow',
        on_delete=models.CASCADE,
        related_name='report_cow',
        null=True,
        blank=True,
        default=uuid.uuid4,
    )
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)  

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name 
