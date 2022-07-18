from django.urls import path
from . import views

app_name='articles_urls'
urlpatterns = [
    path("",views.articles_list,name='list'),
    path("create",views.articles_create,name='create'),
    path('<article_slug>',views.articles_detile,name='detail'),
]
