from django.urls import path
from .views import PostListView, PostCreateView, UserProfileView
from . import views
from . models import Post

urlpatterns = [
    path('', PostListView.as_view(), name='posts-home' ),
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('topic/post/new/', views.TopicPostCreateView.as_view(), name='topic-post-create'),
    path('profile2/<str:username>/', UserProfileView.as_view(), name='profile2'),
    path('search', views.search, name='search'),
    path('like/<int:post_id>/', views.like_post, name='like-post'),
    path('follow', views.follow, name='follow'),
    path('followers/<str:username>/', views.followers_list, name='followers-list'),
    path('frames/', views.frames, name='frames'),
    path('topics/technology/', views.technology, name='technology-posts'),
    path('topics/animals/', views.animals, name='animals-posts'),
    path('topics/automobiles/', views.automobiles, name='automobiles-posts'),
    path('topics/humour/', views.humour, name='humour-posts'),
    path('topics/nature/', views.nature, name='nature-posts'),
    path('topics/news/', views.news, name='news-posts'),
    path('topics/money/', views.money, name='money-posts'),
    path('topics/entertainment/', views.entertainment, name='entertainment-posts'),
    path('topics/motivational/', views.motivational, name='motivational-posts'),
    path('topics/sports/', views.sports, name='sports-posts'),
    path('topics/art/', views.art, name='art-posts'),
    path('topics/clips/', views.clips, name='clips-posts'),
]