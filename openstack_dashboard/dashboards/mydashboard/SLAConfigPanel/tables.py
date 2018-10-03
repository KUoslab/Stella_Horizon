from django.utils.translation import ugettext_lazy as _

from horizon import tables


class MyFilterAction(tables.FilterAction):
    name = "myfilter"


class InstancesTable(tables.DataTable):
    name = tables.Column('name', \
                         verbose_name=_("Name"))
    status = tables.Column('status', \
                           verbose_name=_("Status"))
    zone = tables.Column('availability_zone', \
                         verbose_name=_("Availability Zone"))
    image_name = tables.Column('image_name', \
                               verbose_name=_("Image Name"))

    class Meta(object):
        name = "instances"
        verbose_name = _("Instances")
        table_actions = (MyFilterAction,)
