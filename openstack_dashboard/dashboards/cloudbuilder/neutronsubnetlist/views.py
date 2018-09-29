from django.utils.datastructures import SortedDict
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import tables
from openstack_dashboard import api

from openstack_dashboard.dashboards.cloudbuilder.neutronsubnetlist import tables as neutronsubnetlisttable

class IndexView(tables.DataTableView):
    # A very simple class-based view...
    table_class = neutronsubnetlisttable.NeutronSubnetListTable
    template_name = 'cloudbuilder/neutronsubnetlist/index.html'

    def get_data(self):
        # Add data to the context here...
        subnets = api.neutron.subnet_list(self.request)
        networks = api.neutron.network_list(self.request)
        netmap = {}
        for n in networks:
            netmap[n.id] = n.name
        for s in subnets:
            s.network_name = netmap[s.network_id]
        return subnets
