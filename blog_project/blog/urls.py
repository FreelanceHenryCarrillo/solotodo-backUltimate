from django.urls import path
from .views import PostListCreate, PostDetail

urlpatterns = [
    path('api/posts/', PostListCreate.as_view(), name='post-list-create'),
    path('api/posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]