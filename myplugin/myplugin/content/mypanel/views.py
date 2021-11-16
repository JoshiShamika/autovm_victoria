from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'identity/mypanel/index.html'
    
    def get_context_data(self, *args, **kwargs):
        data = {
            'network incoming bytes': 10646, 
            'network outgoing bytes': 10586, 
            'disk device write bytes': 46475264, 
            'network outgoing packets': 116, 
            'memory usage': 14.609375, 
            'disk device read requests': 1041, 
            'network incoming packets': 101, 
            'cpu': 175930000000, 
            'disk device write requests': 705, 
            'disk device read bytes': 21753344, 
            'image download': 12716032, 
            'image serve': 12716032
            }
        context = data
        return context