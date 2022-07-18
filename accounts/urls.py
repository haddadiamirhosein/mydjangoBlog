from django.urls import path
from . import views

app_name='accounts_urls'

urlpatterns = [
    path("signup/",views.signup_views,name='signup'),
    path("login/",views.login_views,name='login'),
    path("logout/",views.logout_views,name='logout'),
]
