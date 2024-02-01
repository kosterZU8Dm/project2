from django.urls import path
from .views import posts_list, main_page, search, contacts, signup, login_view

urlpatterns = [
    path('posts_list/', posts_list, name='posts_list'),
    path('', main_page, name='main_page'),
    path('contacts/', contacts, name='contacts'),
    path('search/', search, name='search'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
]