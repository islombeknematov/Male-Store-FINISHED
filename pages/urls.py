from django.urls import path

from pages.views import ContactCreateView, IndexTemplateView, AboutTemplateView

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('', IndexTemplateView.as_view(), name='home'),
]

