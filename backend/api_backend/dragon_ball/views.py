# dragon_ball/views.py
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views import View

from dragon_ball.forms import dragonballForm, dragonballsagaForm, dragonballvivoForm, UserForm
from dragon_ball.models import Dragonball, Dragonballsaga, Dragonballvivo
from dragon_ball.serializers import DragonballSerializer, DragonballsagaSerializer, DragonballvivoSerializer
from django.middleware.csrf import get_token

def get_all_dragonball():
    dragonballs = Dragonball.objects.all().order_by('name')
    dragonball_serializers = DragonballSerializer(dragonballs, many=True)
    return dragonball_serializers.data

def get_all_dragonballsagas():
    dragonballsagas = Dragonballsaga.objects.all().order_by('name')
    dragonballsagas_serializers = DragonballsagaSerializer(dragonballsagas, many=True)
    return dragonballsagas_serializers.data

def get_all_dragonballvivos():
    dragonballvivos = Dragonballvivo.objects.all().order_by('name')
    dragonballvivos_serializers = DragonballvivoSerializer(dragonballvivos, many=True)
    return dragonballvivos_serializers.data

def dragonball_rest(request):
    dragonballs = get_all_dragonball()
    return JsonResponse(dragonballs, safe=False) 

def dragonballsaga_rest(request):
    dragonballsagas = get_all_dragonballsagas()
    return JsonResponse(dragonballsagas, safe=False) 

def dragonballvivo_rest(request):
    dragonballvivos = get_all_dragonballvivos()
    return JsonResponse(dragonballvivos, safe=False)

def indexdb(request):
    dragonballs = get_all_dragonball()
    dragonballsagas = get_all_dragonballsagas()
    dragonballvivos = get_all_dragonballvivos()
    return render(request, 'indexdb.html', {'dragonballs': dragonballs, 'dragonballsagas':dragonballsagas, 'dragonballvivos':dragonballvivos})

class dragonballView(CreateView):
    form_class = dragonballForm
    template_name = 'form_dragonball.html'
    success_url = '/'

class dragonballsagaView(CreateView):
    form_class = dragonballsagaForm
    template_name = 'form_dragonballsaga.html'
    success_url = '/'

class dragonballvivoView(CreateView):
    form_class = dragonballvivoForm
    template_name = 'form_dragonballvivo.html'
    success_url = '/'

class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'form_dragonballuser.html'
    success_url = '/'

def users_rest(request):
    return JsonResponse("Ok", safe=False)




