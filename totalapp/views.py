# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	return HttpResponse("Hello, world. You're at the poll index.")

def homepage(request):
	return HttpResponse("homepage.")

def album(request, album_id):
	return HttpResponse("album page.")

def login_main_page(request):
    return render_to_response('mainpage.html', RequestContext(request))

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/l/')
