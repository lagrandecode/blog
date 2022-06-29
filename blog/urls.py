
from sqlite3 import connect
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('connect/', include('connect.urls')),

]
