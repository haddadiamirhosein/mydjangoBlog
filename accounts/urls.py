from django.urls import path
from . import views

app_name='accounts_urls'

urlpatterns = [
    path("signup/",views.signup_views,name='signup'),
]
