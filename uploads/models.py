from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Document(models.Model):
    PAPER_CHOICES = [
        ('past_paper', 'Past Paper'),
        ('solution', 'Solution'),
        ('note', 'Note'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='documents/')
    document_type = models.CharField(max_length=20, choices=PAPER_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
