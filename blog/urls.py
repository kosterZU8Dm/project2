from django.urls import path
from .views import post_list, main_page, search, contacts

urlpatterns = [
    path('post_list/', post_list, name='post_list'),
    path('', main_page, name='main_page'),
    path('contacts/', contacts, name='contacts'),
    path('search/', search, name='search'),
]