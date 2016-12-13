from django.conf.urls import url
from django.contrib.auth.views import logout
from . import views

app_name = 'shop'

urlpatterns = [
    # 127.0.0.1:8000/
    url(r'^$', views.index, name='index'),

    # 127.0.0.1:8000/register/
    url(r'^register/$', views.register, name='register'),

    # 127.0.0.1:8000/store/
    url(r'^store/$', views.store, name='store'),
]
