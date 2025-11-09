from django.urls import path, include
from . import views

urlpatterns = [
    path('luke_skywalker/', views.get_luke_info),
    path('X-wing/', views.get_X_wing),
    #path('next-starship/', views.get_next_starship)
]

