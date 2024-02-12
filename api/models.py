from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.


class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        # Hash password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def _str_(self):
        return self.email
    



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    target_amount = models.FloatField()
    raised_sofar = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    account_number = models.CharField(max_length=100)
    upi_id = models.CharField(max_length=100)
    Images = models.ImageField(upload_to='images/',default='')

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Donation(models.Model):
    amount = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    def __str__(self):
        return str( self.project.title ) 
    


