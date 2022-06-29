
from sqlite3 import connect
from django.contrib import admin
from django.urls import path, include
from connect.views import question_list, question_retrieve
from connect.views import question_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', question_list),
    path('retrieve/<pk>/', question_retrieve),
    path('create/',question_create)
] 
