from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.stella import dashboard


class ConfigPanel(horizon.Panel):
    name = _("Configuration")
    slug = "SLAConfigPanel"

dashboard.StellaDashboard.register(ConfigPanel)
