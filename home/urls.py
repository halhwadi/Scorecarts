from django.contrib import admin
from django.urls import path, include, re_path
import os
import sys
import django
from home import views

sys.path.append(os.path.abspath(r'C:\Users\Husam.Alhwadi\django_projects\scorecarts'))  # path to your django project

# Specify settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scorecarts.settings')

# Setup Django
django.setup()

urlpatterns = [
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('create_ticket', views.create_ticket, name='create_ticket'),
    path('tickets_list', views.tickets_list, name='tickets_list'),
    path('view_ticket/<int:id>', views.view_ticket, name='view_ticket'),
    path('update_ticket/<int:id>', views.update_ticket, name='update_ticket'),
    path('delete_ticket/<int:id>', views.delete_ticket, name='delete_ticket')
]