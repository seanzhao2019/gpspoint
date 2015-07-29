from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from userdata.models import Userdata
def index(request):
    
    try:
        if request.method=='GET':
            #print request.GET

			#user_id_get=request.POST.get('user_id')
            username_get=request.GET.get('username')
         
            print username_get
            user_dict=Userdata.objects.filter(username=username_get).values()
            print user_dict[0]

            return render(request,'waypoint/index.html',{'user_dict':user_dict[0]})

    except:
        print 'something wrong'
        
    return render(request,'waypoint/index.html')


