from django import forms
from django.core.exceptions import ValidationError

class UploadForm(forms.Form):
    file = forms.FileField()
    FILE_MAX_SIZE = 1024
    ALLOWED_TYPES = ['txt']

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)


    def getFile(self):
        file = self.cleaned_data['file']
        '''if file:
            if len(file.name.split('.')) == 1:
                raise forms.ValidationError(_('File type is not supported'), code = 'invalid')

            file_type = file.name.split('.')[1]
            # print file_type
            if file_type in self.ALLOWED_TYPES:
                if file._size > self.FILE_MAX_SIZE:
                    raise forms.ValidationError(_('Please keep filesize \
                            under %s. Current filesize %s') % \
                            (filesizeformat(settings.self.FILE_MAX_SIZE),\
                            filesizeformat(file._size)))
            else:
                raise forms.ValidationError('unsupported type')'''

        return file
