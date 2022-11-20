from django.views.generic import TemplateView

from .services import get_term


class Homepage(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link'] = 'https://spacepython.pythonanywhere.com/'
        context['term'] = get_term()
        return context
