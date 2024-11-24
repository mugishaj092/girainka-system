from django.db import models
import uuid

class Cow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    owner = models.OneToOneField(
        'members.User',
        on_delete=models.CASCADE,
        related_name='cow',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name