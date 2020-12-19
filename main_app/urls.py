from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for finches index
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    # new route used to show a form and create a finch
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
]