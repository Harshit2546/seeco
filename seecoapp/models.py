from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=10)
    comment=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name