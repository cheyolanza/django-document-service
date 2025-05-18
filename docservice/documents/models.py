from django.db import models

# Create your models here.
class Document(models.Model):
    file = models.FileField(upload_to="documents/")
    name = models.CharField(max_length=255)
    upload_at = models.DateTimeField(auto_now_add=True)
    size = models.PositiveBigIntegerField()
    content_type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name