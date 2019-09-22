from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from my_app.models import blog


class HomeView(LoginRequiredMixin, ListView):
    model = blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'
    ordering = ['-publish_date']
    paginate_by = 3


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = blog
    template_name = 'blog/blog_detail.html'


class CreateBlogView(LoginRequiredMixin, CreateView):
    model = blog
    template_name = 'blog/create_blog.html'
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)