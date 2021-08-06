from django.http import request
from django.shortcuts import render

# Create your views here.
def skill(request):
    context={'skill': 'active'}
    return render(request,'edu/skill.html',context)