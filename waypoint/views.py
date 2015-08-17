from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from userdata.models import Userdata,Sensordata
def index(request):
    
    try:
        if request.method=='GET':
            #print request.GET
            username_get=request.GET.get('username')
            user_id_get=request.GET.get('user_id')      
            print username_get,user_id_get
            
            user_all=Userdata.objects.all()
            print user_all

            usercount=Userdata.objects.filter(username=username_get).count()
            print usercount

            lanlon_list=[]
            heart_rate_list=[]
            health_info_list=[]
            all_lanlon_list=[]      
            all_heart_rate_list=[]
            all_health_info_list=[]

            if user_id_get :
                a_dict=Userdata.objects.filter(username=username_get)
                user_dict=a_dict.filter(user_id=user_id_get)   #user_dict.values()is necessnary
                usercount1=user_dict.count()
                print a_dict
                print user_dict,usercount1
                             
                u_pk=user_dict[0].id
                print u_pk
                sensor=Sensordata.objects.filter(user=u_pk).order_by('timestamp')
		print sensor
                lanlon_list.append((sensor.last().lan,sensor.last().lon))  
                heart_rate_list.append(sensor.last().heart_rate)
                heart_rate=sensor.last().heart_rate
                print lanlon_list,heart_rate_list
                if heart_rate<60:
                    health_info_list.append(0)
                elif heart_rate>100:
                    health_info_list.append(1)
                else:
                    health_info_list.append(2)
                print health_info_list


            else:
                user_dict=Userdata.objects.filter(username=username_get)    #user_dict.values()is necessnary
                u_pk_list=[]
                print user_dict,usercount
		for i in user_dict:      
                    a=i.id
                    print i,a
                    u_pk_list.append(a)
                print u_pk_list
        	for i in u_pk_list:
		    sensor=Sensordata.objects.filter(user=i).order_by('timestamp')
                    print sensor   
                    if sensor.count()>0:
                        lanlon_list.append((sensor.last().lan,sensor.last().lon))
                        a=(sensor.last().lan+0.005,sensor.last().lon+0.005)
                        heart_rate_list.append(sensor.last().heart_rate)
                        b=sensor.first().heart_rate
                        print lanlon_list,heart_rate_list
                        if sensor.last().heart_rate<60 :
                            health_info_list.append(0)
                        elif sensor.last().heart_rate>100:
                            health_info_list.append(1)
                        else:
                            health_info_list.append(2)
#                print health_info_list
                    else:
                        lanlon_list.append(a)
                        heart_rate_list.append(b)
                        if b<60:
                            health_info_list.append(0)
                        elif b>100:
                            health_info_list.append(1)
                        else:
                            health_info_list.append(2)
                print health_info_list

                usercount1=1
                a_pk_list=[]
                for i in user_all:
                    print i
                    d=i.id
                    print i,d
                    a_pk_list.append(d)
                print a_pk_list
                for i in a_pk_list:
                    allsensor=Sensordata.objects.filter(user=i).order_by('timestamp')
                    print allsensor,allsensor.count()
                    if allsensor.count()>0:
                        print allsensor.count()
                        all_lanlon_list.append((allsensor.last().lan,allsensor.last().lon))
                        c=(allsensor.last().lan+0.005,allsensor.last().lon+0.005)
                        print all_lanlon_list

                        all_heart_rate_list.append(allsensor.last().heart_rate)
                        d=allsensor.first().heart_rate

                        if allsensor.last().heart_rate<60 :
                            all_health_info_list.append(0)
                        elif allsensor.last().heart_rate>100:
                            all_health_info_list.append(1)
                        else:
                            all_health_info_list.append(2)
#                    print all_heart_rate_list,all_health_info_list

                        
                    else:
                        all_lanlon_list.append(c)
                        all_heart_rate_list.append(d)
                        print all_lanlon_list

                        if d<60:
                            all_health_info_list.append(0)
                        elif d>100:
                            all_health_info_list.append(1)
                        else:
                            all_health_info_list.append(2)
                print all_heart_rate_list,all_health_info_list




 
        return render(request,'waypoint/index.html',{'user_dict':user_dict,'usercount':usercount,'lanlon':lanlon_list,'user_all':user_all,'all_lanlon':all_lanlon_list,'heart_rate':heart_rate_list,'usercount1':usercount1,'health_info':health_info_list,'all_heart_rate':all_heart_rate_list,'all_health_info':all_health_info_list})

    except:
        print 'something wrong'
        
    return render(request,'waypoint/index.html')

def hello(request):
	return render(request,'waypoint/hello.html')
