from django.shortcuts import render
from django.http import HttpResponse
from django.utils import simplejson
from models import *
from django.views.generic import View
from django.core import serializers

class ClientView(View):
    def get(self, request, *args, **kwargs):
        client=Client()
        client.save()
        data = simplejson.dumps({'token': client.token})
        return HttpResponse(data, mimetype='application/json')

class PairView(View):
    def post(self, request, *args, **kwargs):
        status=True
        client=Client.objects.get(token=request.POST.get('token',''))
        tuplePair=Pair.objects.get_or_create(client=client,key=request.POST.get('key',''))
        pair=tuplePair[0]
        pair.value=request.POST.get('value','')
        # pair=Pair(client=client,key=request.POST.get('key',''),value=request.POST.get('value',''))
        try:
            pair.save()
        except Exception, e:
            status=False
        data = simplejson.dumps({'status': status})
        return HttpResponse(data, mimetype='application/json')

    def get(self, request, *args, **kwargs):
        client=Client.objects.get(token=request.GET.get('token',''))
        if 'key' in request.GET:
            pair=Pair.objects.get(client=client,key=request.GET.get('key',''))
            data = simplejson.dumps({'value': pair.value})
        else:
            pairs=Pair.objects.filter(client=client)
            data = serializers.serialize('json',pairs, indent=2,)
        return HttpResponse(data, mimetype='application/json')
    