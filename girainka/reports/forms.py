from django import forms
from .models import Report
from django.core.exceptions import ValidationError

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['full_name', 'email', 'phone', 'address', 'message', 'cow_id']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }

    def save(self, commit=True):
        
        instance = super().save(commit=False)
        if not self.user.is_authenticated:
            raise ValidationError("User is not logged in.")
        instance.user_id = self.user
        
        if commit:
            instance.save()
        return instance
