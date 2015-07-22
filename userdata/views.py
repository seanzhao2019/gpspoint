from django.shortcuts import render
import json as simplejson
from django.views.decorators.csrf import csrf_exempt  
from django.http import HttpResponse
from models import Userdata
# Create your views here.
#20150721
@csrf_exempt
def get_userdata(request):
    
    try:
    	if request.method=='POST':
	    user_id=request.POST.get('user_id')
	    username=request.POST.get('username')
	    gender=request.POST.get('gender')
	    age=request.POST.get('age')  
	    blood_type=request.POST.get('blood_type') 
	    emergency_number=request.POST.get('emergency_number')  
	    destination=request.POST.get('destination')     	
	    userdata=Userdata()
	    userdata.user_id=user_id
            userdata.username=username
            userdata.gender=gender
            userdata.age=age
            userdata.blood_type=blood_type
            userdata.emergency_number=emergency_number
            userdata.destination=destination
	    userdata.save()
	    a= Userdata.objects.all()
	    print a
	    return HttpResponse('userdata')
    except:
	print 'something wrong'
        
    return HttpResponse('ok')

