from django.shortcuts import get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from blog.models import PostModel

from blog.forms import CommentModelForm



class BlogListView(ListView):
    template_name = 'blog.html'
    # queryset = PostModel.objects.order_by('-pk')
    paginate_by = 2

    def get_queryset(self):
        print(self.request.GET)
        qs = PostModel.objects.order_by('pk')
        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tags__title=tag)
        return qs



class BlogDetailView(DetailView):
    template_name = 'blog-detail.html'
    model = PostModel



class CommentCreateView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)


    def get_success_url(self):              # SAME
        return reverse('blog:detail', kwargs={'pk': self.kwargs.get('pk')})
                         # reverse IN VIEWS
                        # url IN TEMPLATE










