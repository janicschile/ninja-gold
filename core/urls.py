from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index_core),
    path('procesar_oro/', views.procesarOro),
]