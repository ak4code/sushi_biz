from django.views.generic import TemplateView, DetailView
from .models import Page


class HomeIndexView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Page.objects.get(is_home__exact=True)
        return context


class PageView(DetailView):
    model = Page
    template_name = 'home/page.html'


class RobotsView(TemplateView):
    template_name = 'home/robots.txt'
    content_type = "text/plain"
