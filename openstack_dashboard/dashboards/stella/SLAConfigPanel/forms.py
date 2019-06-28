from django import forms

import requests
from requests.auth import HTTPDigestAuth
import json

URLServer = "http://203.230.60.81:5000"
URLstatus = "/stella"
URLlistVM = "/stella/vms"
URLSetSLA = "/stella/vms/sla"
URLHypervisor = "/stella/hypervisor"

HEADERS = {
    'Content-Type': 'application/json; charset=utf-8',
}

class PostForm(forms.Form):
    VM_name = forms.CharField()
    SLO_Option = forms.CharField()
    SLO_Value = forms.IntegerField(min_value=1)

    def submitSLA(self, request):
        #print(request.POST['VM_name'])
        #print(request.POST['SLA_Option'])
        #print(request.POST['SLA_Value'])
        URL = URLServer + URLSetSLA
        print(URL)
        print(URL)
        print(URL)
        print(URL)
        _VM_name = request.POST['VM_name']
        _SLO_Option = request.POST['SLO_Option']
        _SLO_Value = request.POST['SLO_Value']
        #Response = requests.get(URL, headers=HEADERS)
        #data = Response.json()
        data = '{"name": "' + _VM_name + '", "SLA_Option": "' + _SLO_Option + '", "SLA_Value": "' + _SLO_Value + '"}'
        response = requests.post(URL , data=data, headers={"Content-Type": "application/json"})
        print(data)
        print(response)
