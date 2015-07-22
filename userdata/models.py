from django.db import models

# Create your models here.
class Userdata(models.Model):
    user_id=models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)    
    age = models.IntegerField()
    blood_type=models.CharField(max_length=6)
    emergency_number = models.IntegerField()
    destination=models.CharField(max_length=20)
    

    def __unicode__(self):
        return self.username

