"""
URL configuration for girainka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from members.views import create_user,login_user
from reports.views import report
from contacts.views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('report/',report,name='report'),
    path('signup/', create_user, name='signup'),
    path('login/', login_user, name='login'),
    path('contact/', contact, name='contact'),
    path('users/', views.users, name='users'),
    path('report_dashboard/', views.report_dashboard, name='report_dashboard'),

    path('dashboard/', views.dashboard, name='contact'),
]
