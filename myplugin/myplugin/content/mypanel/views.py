from django.views import generic
import json


class IndexView(generic.TemplateView):
    template_name = 'identity/mypanel/index.html'
    
    def get_context_data(self, *args, **kwargs):
        data = {
            'disk.device.write.requests': 783, 
            'network.outgoing.bytes': 15698, 
            'network.incoming.packets': 283, 
            'disk.device.write.bytes': 46624768, 
            'disk.device.read.requests': 1042, 
            'memory.usage': 14.546875, 
            'disk.device.read.bytes': 21754368, 
            'network.incoming.bytes': 26542, 
            'cpu': 1665930000000, 
            'network.outgoing.packets': 152
        }
        
        context = data
        return context