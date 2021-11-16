from django.views import generic
import json


class IndexView(generic.TemplateView):
    template_name = 'identity/mypanel/index.html'
    
    def get_context_data(self, *args, **kwargs):
        data = {}
        with open('ceiltest') as f:
            lines = f.readlines()
            for line in reversed(lines):
                key = (json.loads(line)['name'])
                if key not in data.keys():
                    data[key] = json.loads(line)['volume']
        context = data
        return context