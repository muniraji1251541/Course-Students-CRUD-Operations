"""
URL configuration for student_register project.

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
from django.contrib import admin
from django.urls import path
from reg.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('student_form/',student_form,name='student_form'),
    path('course_list/',course_list,name='course_list'),
    path('course_list/<int:pk>',students,name='students'),
    path('course_list/<int:pk>/<int:id>',student_details,name='student_details'),
    path('search',search,name='search'),
    path('student_update/<int:pk>',student_form,name='student_update'),
    path('student_delete/<int:pk>',student_delete,name='student_delete'),
]
