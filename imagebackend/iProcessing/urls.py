from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('process',views.imageProcessing,name="processImage"),
    path('',views.imageProcessing),

] +static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
