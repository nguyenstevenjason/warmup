# Create your views here.
from django.http import HttpResponse
from django.utils import simplejson
from counter.models import *
from counter.modelTests import *
import unittest
import StringIO
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render_to_response('client.html', {})

def login_view(request):
    try:
        dic = simplejson.loads(request.body)
    except KeyError:
        return request.send_error(500)
    try:
        user = dic["user"]
        password = dic["password"]
    except:
        return request.send_error(500)
    errCode = login(user, password)
    if errCode < 0:
        resp = {"errCode": errCode}
    else:
        resp = {"errCode": SUCCESS, "count": errCode}
    return HttpResponse(simplejson.dumps(resp), content_type = "application/json")
    
def add_view(request):
    try:
        dic = simplejson.loads(request.body)
    except KeyError:
        return request.send_error(500)
    try:
        user = dic["user"]
        password = dic["password"]
    except:
        return request.send_error(500)
    errCode = add(user, password)
    if errCode < 0:
        resp = {"errCode": errCode}
    else:
        resp = {"errCode": SUCCESS, "count": errCode}
    return HttpResponse(simplejson.dumps(resp), content_type = "application/json")

@csrf_exempt
def resetFixture_view(request):
    errCode = TESTAPI_resetFixture()
    resp = {"errCode": errCode}
    return HttpResponse(simplejson.dumps(resp), content_type = "application/json")

def unitTests_view(request):
    buffer = StringIO.StringIO()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestModels)
    result = unittest.TextTestRunner(stream = buffer, verbosity = 2).run(suite)
    
    rv = {"totalTests": result.testsRun, "nrFailed": len(result.failures), "output": buffer.getvalue()}
    return HttpResponse(simplejson.dumps(rv), content_type = "application/json")