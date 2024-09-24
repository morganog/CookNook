from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cooknook-home'),
    path('about/', views.about, name='cooknook-about'),
    path('account/', views.account, name='cooknook-account'),
]

