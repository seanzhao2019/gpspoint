from django.shortcuts import render ,redirect
import json as simplejson
from django.views.decorators.csrf import csrf_exempt  
from django.http import HttpResponse
from models import Userdata , Sensordata
# Create your views here.

@csrf_exempt
def Get_userdata(request):
    
    try:
    	if request.method=='POST':
	    print request.POST
#get the querydict of post ------userdata
	    user_id_get=request.POST.get('user_id')
	    username_get=request.POST.get('username')
	    gender_get=request.POST.get('gender')
	    age_get=request.POST.get('age') 
	    blood_type_get=request.POST.get('blood_type') 
	    emergency_number_get=request.POST.get('emergency_number')  
	    destination_get=request.POST.get('destination')     	

	    update_userdata=Userdata.objects.update_or_create(user_id=user_id_get,
							username=username_get,
							defaults={'gender':gender_get,
							'age':age_get,
							'blood_type':blood_type_get,
							'emergency_number':emergency_number_get,
							'destination':destination_get})

#	    if update_userdata[1]:
#		print update_userdata[0].id
		
#	    else:
#		print update_userdata[0].id

	return HttpResponse(update_userdata[0].id)

    except:
	print 'something wrong'
        
    return HttpResponse('ERROR')


@csrf_exempt
def Get_sensordata(request):

    try:
    	if request.method=='POST':
	    print request.POST
#get the querydict of post ------sensordata
	    user_id_list=request.POST.getlist('user_id')
	    timestamp_list=request.POST.getlist('timestamp')
	    lan_list=request.POST.getlist('lan')
	    lon_list=request.POST.getlist('lon')
	    heart_rate_list=request.POST.getlist('heart_rate')
<<<<<<< HEAD

=======
>>>>>>> 9feab6ed4c2480c55945e9b6496155b94be49b64
	  
#calculate the length------sensordata
	    l1=len(user_id_list)
	    l2=len(timestamp_list)
	    l3=len(lan_list)
	    l4=len(lon_list)
	    l5=len(heart_rate_list)
#	    l6=len(emergency_number_list)
#	    l7=len(destination_list)
	    
	    L=[]    #list of length
	    L.append(l1)
	    L.append(l2)
	    L.append(l3)
	    L.append(l4)
	    L.append(l5)
#	    L.append(l6)
#	    L.append(l7)
	    
	    compare_list=[]   #compare the items of L, it must have the same number ,if not append 0
	    for i in L:       #else append 1,then compare the result ,if the minimum is 0,drop the userdata
		for j in L:
		    if i==j:
			compare_list.append(1)
		    else:
			compare_list.append(0)
#	    print compare_list,len(compare_list)
	    if min(compare_list)==1:
		i=0		
		while (i<l1):
		    get_sensordata=Sensordata()
		    get_sensordata.user_id=user_id_list[i]
	    	    get_sensordata.timestamp=timestamp_list[i]         
            	    get_sensordata.lan=lan_list[i]
            	    get_sensordata.lon=lon_list[i]
            	    get_sensordata.heart_rate=heart_rate_list[i]
#            	    get_sensordata.emergency_number=emergency_number_list[i]
#            	    get_sensordata.destination=destination_list[i]
	    	    get_sensordata.save()
		    i=i+1
#		print Sensordata.objects.all()
#		print Sensordata.id
	    	return HttpResponse('Successful !')
	    else:
	    	return HttpResponse('You need transmit again !')

    except:
	print 'something wrong'
        
    return HttpResponse('ERROR')

	
