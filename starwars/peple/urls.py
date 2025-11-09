from django.urls import path, include
from . import views

urlpatterns = [
    path('luke_skywalker/', views.get_luke_info),
    path('X-wing/', views.get_X_wing),
    
]

