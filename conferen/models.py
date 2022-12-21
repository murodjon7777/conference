from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150)
    img=models.URLField()
    text=models.TextField()
    file=models.FileField()
    
    
    def __str__(self) -> str:
        return self.title
