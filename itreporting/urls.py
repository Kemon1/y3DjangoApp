from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

app_name = 'itreporting'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('report/', PostListView.as_view(), name = 'report'),
    path('issues/<int:pk>', PostDetailView.as_view(), name = 'issue-detail'),
    path('issue/new', PostCreateView.as_view(), name = 'issue-create'),
    path('issues/<int:pk>/update/', PostUpdateView.as_view(), name = 'issue-update'),
    path('issues/<int:pk>/delete/', PostDeleteView.as_view(), name = 'issue-delete'),
    path('issues/<str:username>', UserPostListView.as_view(), name = 'user-issues'),
]