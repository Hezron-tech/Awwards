
from . import views
from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static
from django_registration.backends.one_step.views import RegistrationView


urlpatterns=[
    path('',views.index,name = 'index'),
    path('search/', views.search, name='search'),
    
    path('profile/',views.profile, name='profile'),
    path('update/<id>', views.update_profile, name='update_profile'),
    path('post/',views.post_project,name='post_project'),
    path('project/(?P<id>\d+)', views.view_project, name='view_project'),
    path('api/v1/projects',views.ProjectList.as_view(),name='projectsEndpoint'),
    re_path(r'^api/projects/$', views.ProjectList.as_view()),
    re_path(r'^api/profiles/$', views.ProfileList.as_view()),
    re_path(r'^api/users/$', views.UserList.as_view()),
    re_path(r'api/awward/project-id/(?P<pk>[0-9]+)/$',
        views.ProjectDescription.as_view()),

    path('logout/', views.logout_user, name='logout'),    
    
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    

    # path('accounts/register/', RegistrationView.as_view(success_url='/profile'),name='django_registration_register'),
    
    

    
    # re_path('accounts/register/',
    #     RegistrationView.as_view(success_url='/profile/'),
    #     name='django_registration_register'),

    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)