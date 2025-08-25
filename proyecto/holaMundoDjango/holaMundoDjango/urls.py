"""
URL configuration for holaMundoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
#from firstApp import views as vista
#from intento import views as vista1

#from firstApp.views import display, displayDatetime
#from intento.views import display as display1

from firstApp import views as firstApp
from secondApp import views as secondApp

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("hola/", vista.display),
    #path("ahora/", vista.displayDatetime),
    #path("", vista.display),
    #path("hola2/", vista1.displayA)
    #path('hola/', display),
    #path('ahora/', displayDatetime),
    #path('hola2/', display1)
    path("firstApp/", include('firstApp.urls')),
    path("secondApp/", include('secondApp.urls'))

]
