from django.urls import path

from . import views

app_name = 'pdf'

urlpatterns = [
    path('', views.index, name='index'),
    path('accept/', views.accept, name='accept'),
    path('resume/<int:id>/', views.resume, name='resume'),
]
