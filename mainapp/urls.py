from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('done/<str:id>', views.done, name='done'),
    path('undone/<str:id>', views.undone, name='undone')
]