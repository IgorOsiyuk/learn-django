# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from .models import Bb, Rubric
from django.views.generic import CreateView
from .forms import BbForm
from django.urls import reverse_lazy
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
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs, 'rubrics':rubrics}

    return render(request,'bboard/index.html', context)

def rubric_bbs(request, rubric_id):
    bbs=Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs':bbs, 'rubrics':rubrics, 'current_rubric':current_rubric}

    return render(request,'bboard/rubric_bbs.html', context)

class BbCreateView(CreateView):
    template_name = 'bboard/bb_create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context