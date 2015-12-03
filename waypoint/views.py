from django.shortcuts import render
from django.http import HttpResponse
from datetime import *
# Create your views here.
from userdata.models import Userdata,Sensordata,Emergencydata
import json
from django.core import serializers
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

            lanlon_uncertain_list=[]
            lanlon_list=[]
            heart_rate_uncertain_list=[]
            heart_rate_list=[]

            health_info_uncertain_list=[]
            health_info_list=[]

            all_lanlon_list=[]      
            all_heart_rate_list=[]
            all_health_info_list=[]

            em_lanlon_list=[]
            em_lanlon_uncertain_list=[]
            em_heart_rate_list=[]
            em_heart_rate_uncertain_list=[]

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
                elif heart_rate>120:
                    health_info_list.append(1)
                else:
                    health_info_list.append(2)
                print health_info_list

#------emergencydata
                
#                em_raw_data=Emergencydata.objects.filter(user=u_pk)
#                em_data=em_raw_data.order_by('-timestamp')
#                em_date=em_raw_data.datetimes('timestamp','minute',order='DESC')
#                print em_date
#                em_stamp=em_date[0]
#                em_lanlon_uncertain_list.append((em_data.first().lan,em_data.first().lon))
#                em_heart_rate_uncertain_list.append(em_data.first().heart_rate)

#                print em_stamp,datetime.now()
#               com_em_stamp=datetime.combine(em_stamp.date(),em_stamp.time())
#                print com_em_stamp
#                timedelta=datetime.now()-com_em_stamp
#                diff_seconds=timedelta.total_seconds()

#                print diff_seconds
#                if diff_seconds< 100:
#                    lanlon_list=em_lanlon_uncertain_list
#                    heart_rate_list=em_heart_rate_uncertain_list
#                    health_info_list.append(0)
#                    print lanlon_list,heart_rate_list
#                else:
#                    lanlon_list=lanlon_uncertain_list
#                    heart_rate_list=heart_rate_uncertain_list
#                    health_info_list=health_info_uncertain_list




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
                        elif b>120:
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
#                center_pk=8
#                center_sensor=Sensordata.objects.filter(user=8).order_by('timestamp')
#                center_lan=center_sensor.last().lan
#                center_lon=center_sensor.last().lon
#                print center_lan,center_lon
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
                        elif allsensor.last().heart_rate>120:
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
                        elif d>120:
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


def test(request):
    user_pk_list=[]
    bd_state_list=[]
    em_lanlon_list=[]
    em_heart_rate_list=[]
    u_id_list=[]    
    for i in Userdata.objects.all():
        user_pk_list.append(i.pk)
    print json.dumps(user_pk_list)


#    for i in user_pk_list:
#        em_raw_data=Emergencydata.objects.filter(user=i)
#        em_raw_data_count=em_raw_data.count()
#        print em_raw_data_count
#        if em_raw_data_count>0:
#            em_data=em_raw_data.order_by('-timestamp')
#            em_time=em_raw_data.datetimes('timestamp','minute',order='DESC')
#            em_stamp=em_time[0]
#            com_em_stamp=datetime.combine(em_stamp.date(),em_stamp.time())
#            timedelta=datetime.now()-com_em_stamp
#            diff_seconds=timedelta.total_seconds()
            
#            if diff_seconds>30:
#                bd_state_list.append(em_data.first().body_state)
#                em_lanlon_list.append((em_data.first().lan,em_data.first().lon))
#                em_heart_rate_list.append(em_data.first().heart_rate)
#                u_id_list.append(i)
#            print em_lanlon_list,bd_state_list,em_heart_rate_list,u_id_list
#        else :
#            pass           
#    text={'u_id':u_id_list,'body_state':bd_state_list,'em_lanlon':em_lanlon_list,'em_heart_rate':em_heart_rate_list}

    em_raw_data=Emergencydata.objects.filter(user=26)
    em_raw_data_count=em_raw_data.count()
    print em_raw_data_count
    if em_raw_data_count>0:
        em_data=em_raw_data.order_by('-timestamp')
        em_time=em_raw_data.datetimes('timestamp','second',order='DESC')
        em_stamp=em_time[0]
        print em_stamp
        com_em_stamp=datetime.combine(em_stamp.date(),em_stamp.time())
        timedelta=datetime.now()-com_em_stamp
        diff_seconds=timedelta.total_seconds()
        print diff_seconds,datetime.now(),com_em_stamp
            
        if diff_seconds<15:
            bd_state=em_data.first().body_state
            em_lanlon=(em_data.first().lan,em_data.first().lon)
            em_heart_rate=em_data.first().heart_rate
            print em_lanlon,bd_state,em_heart_rate
            text=bd_state
        else :
            text=0           
    else:
        pass

    print text

    fr=open('waypoint/templates/waypoint/001.html','r+')
#    fr.write(text)
    json.dump(text,fr)
    fr.close()

    return render(request,'waypoint/001.html')

