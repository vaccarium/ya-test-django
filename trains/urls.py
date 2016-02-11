"""trains URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.utils.timezone import now
from trainsapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^train/(\d+)/$', views.show_train, name='show_train'),
    url(r'^station/(\d+)/(\d{4})/(\d{1,2})/$', views.show_station, name='show_station'),
    url(r'^station/(\d+)/$', views.show_station, {'year': now().year, 'month': now().month}, name='show_station'),

    url(r'^route/(\d+)/(\d+)/$', views.route, name='route'),

    url(r'^$', views.main_page),
]
