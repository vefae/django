from django.conf.urls import url
from first_app import views

urlpatterns = [
    #url('', views.index, name='index'),
    url('help', views.help, name='help'),
    url('', views.users, name='users'),

]
