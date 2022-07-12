
from sqlite3 import connect
from django.contrib import admin
from django.urls import path, include
from connect.views import (question_list, question_retrieve, question_create, question_update, question_delete)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', question_list),
    path('retrieve/<pk>/', question_retrieve),
    path('create/',question_create),
    path('retrieve/<pk>/edit/', question_update),
    path('retrieve/<pk>/delete/', question_delete)
]    
