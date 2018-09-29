from django.utils.translation import ugettext_lazy as _

import horizon

class NeutronPanels(horizon.PanelGroup):
    name = _("Neutron")
    slug = "cloudbuilderneutron"
    panels = ('neutronportlist',)
    default_panel = 'neutronportlist'

class CloudBuilderDashboard(horizon.Dashboard):
    name = _("cloudbuilder.in")
    slug = "cloudbuilder"
    panels = (NeutronPanels,)
    default_panel = 'neutronportlist'

horizon.register(CloudBuilderDashboard)
