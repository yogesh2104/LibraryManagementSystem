from django.db import models

# Create your models here.
class Books(models.Model):
    name=models.CharField(max_length=50)
    isbn=models.CharField(max_length=13)
    author=models.CharField(max_length=80)
    description=models.TextField()
    publishers=models.CharField(max_length=50)

    def __str__(self):
        return self.name