from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.stella import dashboard

class ShowPanel(horizon.Panel):
    name = _("Show SLO")
    slug = "SLAShowPanel"


dashboard.StellaDashboard.register(ShowPanel)
