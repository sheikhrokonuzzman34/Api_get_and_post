from django.urls import path
from .views import *

urlpatterns = [
   path('',home,name='home'),
   path('aaa',student_details,name='aaa'),
   path('bbb',student_list,name='bbb'),
   path('student_create/',student_create,name='student_create'),
   

]