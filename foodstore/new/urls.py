from django.urls import path

from .views import (index, posts_by_category, post_detail, add_post,
                    update_post, delete_post, register, login_view,
                    logout_view)

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', posts_by_category, name='posts_by_category'),

    path('posts/<int:pk>/', post_detail, name='detail'),
    path('posts/<int:pk>/update/', update_post, name='update_post'),
    path('posts/<int:pk>/delete/', delete_post, name='delete_post'),

    path('add-post/', add_post, name='add_post'),

    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]