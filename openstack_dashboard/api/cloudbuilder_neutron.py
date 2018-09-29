from openstack_dashboard.api import neutron

def get_network_name_mapping_for_tenant(request, tenant_id, **params):
    networks = neutron.network_list_for_tenant(request, tenant_id, **params)
    return create_network_name_mapping(networks)

def get_network_name_mapping(request, **params):
    networks = neutron.network_list(request, **params)
    return create_network_name_mapping(networks)

def create_network_name_mapping(networks):
    network_name_map = {}
    for n in networks:
        network_name_map[n.id] = n.name
    return network_name_map
