import requests
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.say_hello, name='hme'),
    path('super/<str:check>', views.superad, name='sup'),
    path('user/<str:check>', views.uuser, name='user'),
    path('register/', views.reg, name='reg'),
    path('process/', views.insert),
    path('rq1/', views.rq1),
    path('acc/', views.accept),
    path('rej/', views.reject),
    path('room/', views.room),
    path('book/', views.book),
    path('recac/', views.get_arecord),
    path('insro/', views.insro),
    path('exp/', views.export1)
]
