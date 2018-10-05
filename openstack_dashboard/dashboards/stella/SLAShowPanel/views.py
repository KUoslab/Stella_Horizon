from horizon import tabs

from openstack_dashboard.dashboards.stella.SLAShowPanel \
    import tabs as mydashboard_tabs

import collections
import logging
import requests
import json

URLServer = "http://api_url"
URLstatus = "/stella"
URLlistVM = "/stella/vms"
URLSetSLA = "/stella/vms/sla"
URLHypervisor = "/stella/hypervisor"

HEADERS = {
    'Content-Type': 'application/json; charset=utf-8',
}

class IndexView(tabs.TabbedTableView):
    tab_group_class = mydashboard_tabs.MypanelTabs
    template_name = 'stella/SLAShowPanel/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        StellaInstances = []
        try:
            print(URL)
        except Exception:
            exceptions.handle(
                self.request,
                _('Unable to retrieve Stella info list.'))

        return StellaInstances