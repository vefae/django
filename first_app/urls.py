from django.conf.urls import url
from first_app import views

#Template tagging
app_name = 'first_app'

urlpatterns = [
    #url('', views.index, name='index'),
    url('login', views.user_login, name='user_login'),
    url('users', views.users, name='users'),
    url('signup', views.signup, name='signup'),
    url('formpage', views.form_name_view, name='form_name'),

]
