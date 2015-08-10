from django.contrib import admin
from userdata.models import Userdata ,Sensordata
# Register your models here.


class UserdataAdmin(admin.ModelAdmin):
    list_display = ('username','user_id','gender','birthday','blood_type','emergency_number','destination')
	#list_filter = ('user')
class SensordataAdmin(admin.ModelAdmin):
    list_display = ('user_id','timestamp','lan','lon','heart_rate')


admin.site.register(Userdata,UserdataAdmin)
admin.site.register(Sensordata,SensordataAdmin)

