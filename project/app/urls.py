from django.urls import path
from .views import *

urlpatterns =[
    path('',Home,name='index'),
    path('register',Registration,name='register'),
    path('showdata',ShowData,name='showdata'),
    path('edit/<pk>',EditData,name='edit'),
    path('update/<pk>',UpdateData,name='update'),
    path('delete/<pk>',DeleteData,name='delete'),
]
