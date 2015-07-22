from django.shortcuts import render
import json
from django.http import HttpResponse
# Create your views here.
/*
def userdata(request):
    dict = {}
    info = 'Data log save success'
    try:
        if request.method == 'POST':
            req = simplejson.loads(request.raw_post_data)
            username = req['username']
            gender = req['gender']
            age = req['age']
            emergency_number = req['emergency_number']
   except:
        import sys
        info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])

    dict['message']=info
    dict['create_at']=str(ctime())
    json=simplejson.dumps(dict)
    return HttpResponse(json)
*/
def index(request):
	return render(request,'index.html')

