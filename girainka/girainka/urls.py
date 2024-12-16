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
from members.views import create_user,login_user,user_dashboard,delete_user,get_user
from reports.views import report,report_dashboard,get_report,delete_report
from contacts.views import contact,message_dashboard,delete_message,get_message
from cows.views import get_cow,delete_cow,cow_dashboard,source_dashboard,get_source,delete_source,add_cow

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('report/',report,name='report'),
    path('signup/', create_user, name='signup'),
    path('login/', login_user, name='login'),
    path('contact/', contact, name='contact'),
    path('dashboard/users/', user_dashboard, name='users'),
    path('dashboard/cows/', cow_dashboard, name='cow'),
    path('dashboard/reports/', report_dashboard, name='report_dashboard'),
    path('delete-user/<uuid:user_id>/', delete_user, name='delete_user'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('get-user/<uuid:user_id>/', get_user, name='get_user'),
    path('get-report/<uuid:report_id>/', get_report, name='get_report'),
    path('delete-report/<uuid:report_id>/', delete_report, name='delete_report'),
    path('get-cow/<uuid:cow_id>/', get_cow, name='get_cow'),
    path('delete-cow/<uuid:cow_id>/', delete_cow, name='delete_cow'),
    path('dashboard/messages/',message_dashboard, name='messages'),
    path('get-message/<uuid:id>/', get_message, name='get_message'),
    path('delete-message/<uuid:id>/', delete_message, name='delete_message'),
    path('source-dashboard/',source_dashboard, name='source_dashboard'),
    path('get-source/<uuid:source_id>/', get_source, name='get_source'),
    path('delete-source/<uuid:source_id>/', delete_source, name='delete_source'),
    path('add-cow/', add_cow, name='add_cow'),
]
