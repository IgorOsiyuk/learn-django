# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from .models import Bb

'''
использую без shortcuts
'''
# def index(request):
#     template = loader.get_template('bboard/index.html')
#     bbs = Bb.objects.order_by('-published')
#     context = {'bbs':bbs}

#     return HttpResponse(template.render(context,request))

'''
использую c shortcuts
'''
def index(request):
    bbs = Bb.objects.order_by('-published')

    return render(request,'bboard/index.html', {'bbs': bbs})