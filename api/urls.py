from django.urls import path
from api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<hash>', views.hash, name='hash'),
    path('<hash>/view', views.view, name='view'),
]
