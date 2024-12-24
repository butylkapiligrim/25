from django.urls import path
from wagnit_blog.apps import WagnitBlogConfig
from wagnit_blog.views import (
    PostListView,
    PostDeleteView,
    PostCreateView,
    PostUpdateView,
    PostDetailView,
)

app_name = WagnitBlogConfig.name

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path("wagnit/", PostListView.as_view(), name="posts_list"),
    path(
        "wagnit/<int:pk>/",
        PostDetailView.as_view(),
        name="posts_detail",
    ),
    path(
        "wagnit/create", PostCreateView.as_view(), name="posts_create"
    ),
    path(
        "wagnit/<int:pk>/update",
        PostUpdateView.as_view(),
        name="posts_update",
    ),
    path(
        "wagnit/<int:pk>/delete",
        PostDeleteView.as_view(),
        name="posts_delete",
    ),
]
