from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('set_language/', views.set_language, name='set_language'),
]
