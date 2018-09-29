from django.utils.translation import ugettext_lazy as _

import horizon
import openstack_dashboard.dashboards.cloudbuilder.dashboard as dashboard


class NeutronPortListPanel(horizon.Panel):
    name = _("Port List")
    slug = "neutronportlist"


dashboard.CloudBuilderDashboard.register(NeutronPortListPanel)
