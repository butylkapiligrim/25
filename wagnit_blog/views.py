from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from wagnit_blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(was_publication=True)


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Post
    fields = (
        "name",
        "description",
        "image",
        "created_at",
        "was_publication",
        "views_counter",
    )
    success_url = reverse_lazy("wagnit_blog:posts_list")


class PostUpdateView(UpdateView):
    model = Post
    fields = (
        "name",
        "description",
        "image",
        "created_at",
        "was_publication",
        "views_counter",
    )
    success_url = reverse_lazy("wagnit_blog:posts_list")

    def get_success_url(self):
        return reverse('wagnit_blog:posts_delete', args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("wagnit_blog:posts_list")
