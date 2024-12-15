from django.db import models
import uuid

class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=False)
    message = models.TextField()
    
    # Change to ForeignKey for many-to-one relationship
    user_id = models.ForeignKey(
        'members.User',  # Assuming 'User' model is in 'members' app
        on_delete=models.CASCADE,
        related_name='reports',  # This will allow access to all reports related to a user
        null=True,
        blank=True,
    )

    # Change to ForeignKey for many-to-one relationship
    cow_id = models.ForeignKey(
        'cows.Cow',  # Assuming 'Cow' model is in 'cows' app
        on_delete=models.CASCADE,
        related_name='reports',  # This will allow access to all reports related to a cow
        null=True,
        blank=True,
    )
    
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)  

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
