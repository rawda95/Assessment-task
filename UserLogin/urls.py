from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import signup, validate_data, profile, logout_user, login_user, home

app_name = 'UserLogin'

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^signup/$', signup, name='signup'),
    url(r'login/$', login_user, name='login_user'),
    url(r'logout/$', logout_user, name='logout_user'),
    url(r'password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    url(r'^validate_username/$', validate_data, name='validate_data'),

    url(r'profile/$', profile, name='profile')

]
