from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('ordermenu/',views.ordermenu,name='ordermenu'),
    #path('contact/',views.contact,name='contact'),
]
