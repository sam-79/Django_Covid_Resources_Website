from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contact', include('contact.urls')),
    path('dashboard', include('dashboard.urls')),
 
    

]