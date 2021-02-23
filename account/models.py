from django.db import models

# Create your models here.
class ManualForm16(models.Model):
    pan_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    date_of_birth = models.DateField() 

    def __str__(self):
        return self.first_name

