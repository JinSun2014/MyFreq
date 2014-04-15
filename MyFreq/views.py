from django.views.generic import TemplateView, FormView
from MyFreq.forms import UploadForm

class IndexView(TemplateView):
    template_name = 'index.html'

class UploadView(FormView):
    form_class = UploadForm
    template_name = 'upload.html'

    def form_valid(self, form):
        file = form.cleaned_data['file']
        print file.read()
        return super(UploadView, self).form_valid(form)

    def get_success_url(self):
        return '/'

    def get_context_data(self, **kwargs):
        context = super(UploadView, self).get_context_data(**kwargs)
        return context
