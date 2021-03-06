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

    # 127.0.0.1:8000/cart/
    url(r'^cart/$', views.cart, name='cart'),

    # 127.0.0.1:8000/deals/
    url(r'^deals/$', views.deals, name='deals'),

    # 127.0.0.1:8000/login/
    url(r'^login/$', views.login_user, name='login_user'),

    # 127.0.0.1:8000/logout/
    url(r'^logout/$', views.logout_user, name='logout_user')
]
