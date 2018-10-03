from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.mydashboard import dashboard


class ConfigPanel(horizon.Panel):
    name = _("Configuration")
    slug = "SLAConfigPanel"


dashboard.StellaDashboard.register(ConfigPanel)
