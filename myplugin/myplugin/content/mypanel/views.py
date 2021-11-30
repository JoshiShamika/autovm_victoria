from django.views import generic
import json


class IndexView(generic.TemplateView):
    template_name = 'identity/mypanel/index.html'
    
    def get_context_data(self, *args, **kwargs):
        user = self.request.user.id
        data = {}
        data1 = {}
        MemoryData = []
        cpuData = []
        Time = []
        count = 0
        timeInt = 300
        prevCPU = 0
        prevMem = 0
        instance = {}
        
        with open('Downloads/ceiltest') as f:
            lines = f.readlines()
            for line in lines:
                if user == json.loads(line)['user_id']:
                    key1 = (json.loads(line)['resource_metadata']['instance_id'])
                    if key1 not in instance.keys():
                        instance[key1] = json.loads(line)['resource_metadata']['display_name']
        
        
        with open('/var/test/ceiltest') as f:
            lines = f.readlines()
            for line in lines:
                key = (json.loads(line)['name']).replace(".", "_")
                if key == 'memory_usage':
                    if prevMem == 0:
                        MemoryData.append(0)
                    else:
                        MemoryData.append(round(json.loads(line)['volume'] - prevMem,2))
                    prevMem = json.loads(line)['volume']
                if key == 'cpu':
                    if prevCPU == 0:
                        cpuData.append(0)
                    else:
                        cpuDiff = (json.loads(line)['volume']/10000000)-prevCPU
                        cpuData.append(round(cpuDiff/timeInt,2))
                    prevCPU = json.loads(line)['volume']/10000000
                    Time.append(count)
                    count = count + 5
                if key not in data1.keys():
                    data1[key] = json.loads(line)['volume']
                    
                    
        with open('/var/test/ceiltest') as f:
            lines = f.readlines()
            for line in reversed(lines):
                if user == json.loads(line)['user_id']:
                    key = (json.loads(line)['name']).replace(".", "_")
                    if key not in data.keys():
                        data[key] = json.loads(line)['volume']
                        if key == 'cpu':
                            time = json.loads(line)['timestamp']
                            time = time.split("T")[-1]
                            hhmm = time.split(":")[0] +":"+ time.split(":")[1]
                            data['timestamp'] = hhmm
                            data['instance'] = json.loads(line)['resource_metadata']['display_name']
                    
        data['cpuData'] = cpuData
        data['MemoryData'] = MemoryData
        data['time'] = Time
        data['cpuPer'] = cpuData[-1]
        data['memPer'] = MemoryData[-1]
        data['min'] = min(cpuData)
        data['max'] = max(cpuData)
        instanceData = {}
        
        for k in instance.keys():
    
            instanceData[instance[k]] = data
        

        
        return {'data':instanceData}