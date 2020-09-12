from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views as blog_views

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('about/', blog_views.about,name='blog-about'),
    path('getassign/', blog_views.ur_assign_view,name='get-assign'),
    #path('generateassign/', blog_views.gen_assign,name='gen-assign'),


]