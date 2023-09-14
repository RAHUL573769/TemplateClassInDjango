from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [path("", views.ViewName.as_view(template_name="base.html"))]
