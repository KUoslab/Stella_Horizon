from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.cloudbuilder import dashboard

class NeutronSubnetListPanel(horizon.Panel):
    name = _("Neutron Subnet List")
    slug = "neutronsubnetlist"


dashboard.CloudBuilderDashboard.register(NeutronSubnetListPanel)
