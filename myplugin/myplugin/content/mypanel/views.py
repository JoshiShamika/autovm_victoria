from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'identity/mypanel/index.html'
    
    def get_context_data(self, *args, **kwargs):
        data = {'message': 'Hello Django!'}
        context = data
        return context