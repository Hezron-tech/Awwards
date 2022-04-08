from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm,RatingsForm,SignUpForm, UpdateProfileForm, UpdateUserForm

from .models import Project,Profile,Rates
from django.urls import reverse

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


@login_required(login_url='/accounts/login/')
def update_profile(request, id):
    profile_object = get_object_or_404(Profile, user_id=id)
    user_object = get_object_or_404(User, id=id)
    profile_form = UpdateProfileForm(request.POST or None, request.FILES, instance=profile_object)
    user_form = UpdateUserForm(request.POST or None, instance=user_object)
    if profile_form.is_valid() and user_form.is_valid():
        profile_form.save()
        user_form.save()
        return HttpResponseRedirect("/profile")

    return render(request, "registration/update_profile.html", {"form": profile_form, "form2": user_form})    


@login_required(login_url='/accounts/login')
def project(request, id):
    project = Project.objects.get(id=id)
    reviews = Rates.objects.all()
    return render(request, 'view-project.html', {"project": project, "reviews": reviews})

@login_required(login_url='/accounts/login')
def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = projectForm(request.POST,request.FILES)
        if form.is_valid():
            post_project = form.save(commit=False)
            post_project.user = current_user
            post_project.save()
            return redirect('index')

        else:
            form = projectForm()
        return render(request,'projects.html',{"form":form})  


@login_required(login_url='/accounts/login')
def view_project(request, id):
    project = Project.objects.get(id=id)
    rate = Rates.objects.filter(user=request.user, project=project).first()
    ratings = Rates.objects.all()
    rating_status = None
    if rate is None:
        rating_status = False
    else:
        rating_status = True
    current_user = request.user
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            review = Rates()
            review.project = project
            review.user = current_user
            review.design = design
            review.usability = usability
            review.content = content
            review.average = (
                review.design + review.usability + review.content)/3
            review.save()
            return HttpResponseRedirect(reverse('view_project', args=(project.id,)))
    else:
        form = RatingsForm()
    params = {
        'project': project,
        'form': form,
        'rating_status': rating_status,
        'reviews': ratings,
        'ratings': rate

    }
    return render(request, 'view-project.html', params)              




