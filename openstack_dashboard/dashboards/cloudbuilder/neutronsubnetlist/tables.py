from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django import template

from horizon import tables

def get_fixed_ips(port):
    template_name = 'project/networks/ports/_port_ips.html'
    context = {"ips": port.fixed_ips}
    return template.loader.render_to_string(template_name, context)


def get_attached(port):
    if port['device_owner']:
        return port['device_owner']
    elif port['device_id']:
        return _('Attached')
    else:
        return _('Detached')

def get_network_link(datum):
	return reverse('horizon:project:networks:detail', kwargs={'network_id': datum.network_id})

class NeutronSubnetListTable(tables.DataTable):
    device_ip = tables.Column("binding:host_id", verbose_name=_("Host"))
    network_id = tables.Column('network_name', verbose_name=_("Network"), link=get_network_link)
    port_status = tables.Column('status', verbose_name=_("Port Status"))
    def __init__(self, request, data=None, needs_form_wrapper=None, **kwargs):
        super(NeutronSubnetListTable, self).__init__(
            request,
            data=data,
            needs_form_wrapper=needs_form_wrapper,
            **kwargs)

    class Meta:
        name = "neutronsubnetlist"
        verbose_name = _("Neutron Subnet List")

