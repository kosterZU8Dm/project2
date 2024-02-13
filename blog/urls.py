from django.urls import path
from .views import posts_list, main_page, search, contacts, signup, login_view, create_post, edit_post, delete_post, view_post
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('posts_list/', posts_list, name='posts_list'),
    path('', main_page, name='main_page'),
    path('contacts/', contacts, name='contacts'),
    path('search/', search, name='search'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='main_page'), name='logout'),
    path('create_post/', create_post, name='create_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('view_post/<int:post_id>/', view_post, name='view_post'),
]