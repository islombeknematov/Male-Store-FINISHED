from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from blog.models import PostModel
from pages.forms import ContactModelForm
from pages.models import BannerModel




class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = PostModel.objects.order_by('-pk')[:3]
        context['banners'] = BannerModel.objects.filter(is_active=True).order_by('-pk')
        return context


class AboutTemplateView(TemplateView):
     template_name = 'about.html'





