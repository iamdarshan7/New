from django.db import models

# Create your models here.
class Pictures(models.Model):
    is_active = models.BooleanField(default=True,unique=True,null=True)
    logo = models.ImageField(upload_to="Images/")
    name= models.CharField(max_length=100)
    

    def __str__(self):
        return self.name