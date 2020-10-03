from django.db import models

# Create your models here.
# Create your models here.
class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, default="")
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=50, default="")
    desc=models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
    


class UserHistory(models.Model):
    username = models.CharField(max_length=50)
    exp=models.CharField(max_length=100)
    salary = models.CharField(max_length=1000)
    
    date = models.DateField()
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username