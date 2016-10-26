"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from trips.views import question_data
from trips.views import register
from trips.views import login
from trips.views import user_input
from trips.views import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^question_data/', question_data, name='question_data'),
	url(r'^register/$', register, name='register'),
	url(r'^login/$', login, name='login'),
	url(r'^user_input/$', user_input, name='user_input'),
	url(r'^logout/$', logout, name='logout'),
]
