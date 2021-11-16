from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'identity/mypanel/index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(IndexView. self).get_context_data(*args, **kwargs)
        context['message'] = 'Hello World!'
        return context