from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Project,Profile,Rates

# Create your views here.

def index(request):
    profile= Profile.objects.all()
    projects= Project.objects.all()
    return render(request,'index.html',{"profile":profile, "projects":projects})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    projects = Project.objects.filter(user=current_user.id).all
    return render(request, 'registration/profile.html', {"projects": projects})


@login_required(login_url='/accounts/login')
def project(request, id):
    project = Project.objects.get(id=id)
    reviews = Rates.objects.all()
    return render(request, 'view-project.html', {"project": project, "reviews": reviews})
