from django.utils import http as utils_http
from django.views import generic
from openstack_dashboard.api.rest import urls
from openstack_dashboard.api.rest import utils as rest_utils
import json

@urls.register
class IndexView(generic.TemplateView):
    url_regex = r"identity/mypanel/myplugin/$"
    
    @rest_utils.ajax(data_required=True)
    def post(self, request):
        data1 = {}
        with open('ceiltest') as f:
            lines = f.readlines()
            for line in reversed(lines):
                key = (json.loads(line)['name']).replace(".", " ")
                if key not in data1.keys():
                    data1[key] = json.loads(line)['volume']
        
        return data1