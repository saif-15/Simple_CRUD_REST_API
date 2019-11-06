"""CRUD_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Rest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/',views.getData,name='get'),
    path('get/<int:id>/',views.getDataById,name='getId'),
    path('post/',views.post_data,name='post_data'),
    path('put/<int:id>/',views.put_data,name='put_data'),
    path('delete/<int:id>/',views.delete_data,name='delete_data'),
    path('delete/',views.delete_data_all,name='delete_data_all')
]
