from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, blank=True,null=True)
    code=models.CharField(max_length=100, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']

class category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name        
