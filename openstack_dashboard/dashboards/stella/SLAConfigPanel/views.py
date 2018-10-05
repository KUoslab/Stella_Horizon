from django.views.generic.edit import FormView
from openstack_dashboard.dashboards.stella.SLAConfigPanel.forms import PostForm

class SLAConfigView(FormView):
    # A very simple class-based view...
    template_name = 'stella/SLAConfigPanel/index.html'
    form_class = PostForm
    success_url = '/stella/'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        context = super(SLAConfigView, self).get_context_data(**kwargs)
        context[VM_name] = VM_name
        print(VM_name)
        context[SLA_Option] = SLA_Option
        print(SLA_Option)
        context[SLA_Value] = SLA_Value
        print(SLA_Value)
        return context
    def form_valid(self, form):
        form.submitSLA(self.request)
        return super(SLAConfigView, self).form_valid(form)