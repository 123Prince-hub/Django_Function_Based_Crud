from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:uid>', views.delete, name='delete'),
    path('<int:uid>', views.update, name='update'),
]