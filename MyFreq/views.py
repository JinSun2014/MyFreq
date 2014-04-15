from django.views.generic import TemplateView, FormView
from MyFreq.forms import UploadForm

class IndexView(TemplateView):
    template_name = 'index.html'

class UploadView(FormView):
    form_class = UploadForm
    template_name = 'upload.html'

    def form_valid(self, form):
        file = form.cleaned_data['file']
        file_content = file.read()
        file_output = open('uploaded/temp', 'w')
        file_output.write(file_content)
        return super(UploadView, self).form_valid(form)

    def get_success_url(self):
        return 'result'

    def get_context_data(self, **kwargs):
        context = super(UploadView, self).get_context_data(**kwargs)
        return context

class ResultView(TemplateView):
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        file_input = open('uploaded/temp', 'r')
        file = file_input.read()
        context['file'] = file
        return context
