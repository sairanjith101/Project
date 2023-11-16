"""
URL configuration for student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from studentApp import views

urlpatterns = [
    path('home/', views.retrieve_view, name='home'),
    path('add/', views.create_view, name='add'),
    path('delete/', views.delete_view, name='delete'),
    path('erase/<id>', views.erase_view, name='erase'),
    path('update/', views.update_view, name='update'),
    path('new/<id>', views.new_view, name='new'),
]
