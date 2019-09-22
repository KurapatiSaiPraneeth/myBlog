from django.urls import path
from .views import HomeView, BlogDetailView, CreateBlogView

urlpatterns = [
    path('', HomeView.as_view(), name="blog-home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name="blog-detail"),
    path('create_blog', CreateBlogView.as_view(success_url="/"), name="create_blog")
]