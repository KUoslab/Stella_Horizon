import collections
import logging

import requests
from requests.auth import HTTPDigestAuth
import json

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

URLServer = "http://203.230.60.81:5000"
URLstatus = "/stella"
URLlistVM = "/stella/vms"
URLSetSLA = "/stella/vms/sla"
URLHypervisor = "/stella/hypervisor"

HEADERS = {
    'Content-Type': 'application/json; charset=utf-8',
}

def StellaStatus(request, search_opts=None, detailed=True):
    URL = URLServer + URLlistVM 
    Response = requests.get(URL , headers=HEADERS)
    data = Response.json()
    
    has_more_data = False
    return (data, has_more_data)


