from stemming.porter2 import stem
from collections import defaultdict
import operator

from django.views.generic import TemplateView, FormView
from MyFreq.forms import UploadForm

class UploadView(FormView):
    form_class = UploadForm
    template_name = 'upload.html'

    def form_valid(self, form):
        file = form.getFile()
        file_content = file.read()
        self.request.session['file'] = file_content
        return super(UploadView, self).form_valid(form)

    def get_success_url(self):
        return 'result'

    def get_context_data(self, **kwargs):
        context = super(UploadView, self).get_context_data(**kwargs)
        return context

class ResultView(TemplateView):
    template_name = 'result.html'

    def handle_file(self, content):
        processed_content = stem(content)
        dict = defaultdict(int)
        for word in processed_content.split():
            dict[word] += 1

        sorted_dict = []
        sorted_dict = sorted(dict.iteritems(), key = operator.itemgetter(1))
        sorted_dict.reverse()

        #for i, (k, v) in enumerate(sorted_dict):
        #    print i, k, v
        return enumerate(sorted_dict[:25])

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        file = self.request.session['file']
        context['file'] = self.request.session['file']
        context['result'] = self.handle_file(file)
        return context
