"""persona_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from persona_app import views

urlpatterns = [
    path('admin/', admin.site.urls, name=''),
    path('', views.persona_list, name='url_persona_list'),
    path('details/<int:id>/', views.persona_details, name='url_persona_details'),
    path('generate/', views.persona_generate, name='url_persona_generate'),
]