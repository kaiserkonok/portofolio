from django.shortcuts import render
from .models import Skill



def home(request):
    return render(request, 'home.html', context={
        'skills': Skill.objects.all()
    })
