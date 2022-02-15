"""scorecarts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
import os
import sys
import django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

sys.path.append(os.path.abspath(r'C:\Users\Husam.Alhwadi\django_projects\scorecarts'))  # path to your django project

# Specify settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scorecarts.settings')

# Setup Django
django.setup()

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
]
