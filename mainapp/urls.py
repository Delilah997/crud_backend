from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name='mainapp_app'
urlpatterns = [
    path('',views.getUsers().as_view()),
    path('create',views.createUser().as_view()),
    path('detail/<pk>',views.detailUser().as_view()),
    path('update/<pk>',views.updateUser().as_view()),
    path('delete/<pk>',views.deleteUser().as_view()),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)