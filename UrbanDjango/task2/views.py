from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def index(request):
    return render(request, 'second_task/class_template.html')


def index2(request):
    return render(request, 'second_task/func_template.html')
