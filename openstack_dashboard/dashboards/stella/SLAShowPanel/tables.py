from django.utils.translation import ugettext_lazy as _

from horizon import tables


class MyFilterAction(tables.FilterAction):
    name = "myfilter"



class InstancesTable(tables.DataTable):
    # In this class, verbose_name is for translation in Horizon UI
    #name = tables.Column('name', verbose_name=_("Name"))
    #status = tables.Column('status', verbose_name=_("Status"))
    #zone = tables.Column('availability_zone', verbose_name=_("Availability Zone"))
    #image_name = tables.Column('image_name', verbose_name=_("Image Name"))
    Stella_Name = tables.Column('name', verbose_name=_("Name"))
    Stella_Hypervisor = tables.Column('hypervisor', verbose_name=_("Hypervisor"))
    Stella_SLAOption = tables.Column('SLA_Option', verbose_name=_("SLA Option"))
    Stella_SLAValue = tables.Column('SLA_Value', verbose_name=_("SLA Value"))
    


    class Meta(object):
        name = "instances"
        verbose_name = _("Instances")
        table_actions = (MyFilterAction,)
