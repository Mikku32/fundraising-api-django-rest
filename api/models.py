from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    target_amount = models.FloatField()
    current_amount = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    account_number = models.CharField(max_length=100)
    upi_id = models.CharField(max_length=100)
    Images = models.ImageField(upload_to='images')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class donation(models.Model):
    amount = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.amount)    

