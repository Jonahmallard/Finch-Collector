from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for finches index
    path('finches/', views.finches_index, name='index'),
]