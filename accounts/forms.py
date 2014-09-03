from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select an img',
        help_text='max. 42 megabytes'
    )
