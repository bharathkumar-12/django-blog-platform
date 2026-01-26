from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PostForm, PostUpdateForm
from .models import Post, Tag
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        qs = Post.objects.all().select_related('author').prefetch_related('tags').order_by('-created_at')
        query = self.request.GET.get('q')
        tag = self.request.GET.get('tag')
        if query:
            qs = qs.filter(Q(title__icontains=query) | Q(body__icontains=query))
        if tag:
            qs = qs.filter(tags__slug=tag)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.select_related('author').prefetch_related('tags')

# Create your views here.
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    form_class = PostUpdateForm

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('home')
