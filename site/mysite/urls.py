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
from django.conf import settings
from django.conf.urls.static import static
from trips.views import question_data
from trips.views import register
from trips.views import login
from trips.views import user_rule
from trips.views import logout
from trips.views import user_test
from trips.views import user_test_UI
from trips.views import chat_js
from trips.views import style_css
from trips.views import log_data

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^question_data/', question_data, name='question_data'),
	url(r'^register/$', register, name='register'),
	url(r'^login/$', login, name='login'),
	url(r'^user_rule/$', user_rule, name='user_rule'),
	url(r'^logout/$', logout, name='logout'),
	url(r'^user_test/$', user_test, name='user_test'),
	url(r'^user_test_UI/.*', user_test_UI, name='user_test_UI'),
	url(r'^chat_js/$', chat_js, name='chat_js'),
	url(r'^log_data/$', log_data, name='log_data'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
