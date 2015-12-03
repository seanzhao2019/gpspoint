from django.db import models

# Create your models here.
class Userdata(models.Model):
    user_id=models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)    
    birthday = models.DateField()
    blood_type=models.CharField(max_length=6)
    emergency_number = models.CharField(max_length=10)
    destination=models.CharField(max_length=20)
    
    class Meta:
        unique_together = (("user_id", "username"),)

    def __unicode__(self):
        return self.username

class Sensordata(models.Model):
    user=models.ForeignKey('Userdata')#Userdata's Primary Key
    timestamp=models.DateTimeField()
    lan=models.FloatField(null=True)
    lon=models.FloatField(null=True)
    heart_rate=models.IntegerField(null=True)

#    def __unicode__(self):
#        return self.user
class Emergencydata(models.Model):
    user=models.ForeignKey('Userdata')#Userdata's Primary Key
    timestamp=models.DateTimeField()
    lan=models.FloatField(null=True)
    lon=models.FloatField(null=True)
    heart_rate=models.IntegerField(null=True)
    body_state=models.IntegerField()#CharField(max_length=3)
#    def __unicode__(self):
#        return self.user

