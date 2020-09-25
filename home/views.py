from django.views.generic import TemplateView
from .models import Page


class HomeIndexView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Page.objects.get(is_home__exact=True)
        return context