from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# class CreateForm(forms.Form):
#
#
#     def __init__(self, *args, **kwargs):
#         super(CreateForm, self).__init__(*args, **kwargs)
#
#         # If you pass FormHelper constructor a form instance
#         # It builds a default layout with all its fields
#         self.helper = FormHelper(self)
#
#         # You can dynamically adjust your layout
#         self.helper.layout.append(Submit('save', 'save'))
#
#
#
#     title = forms.CharField(error_messages={'required': 'Please let us know what to call you!'})
#     email_field = forms.EmailField(error_messages={'required': 'Please let us know what to call you!'})
#     body = forms.CharField(widget=forms.Textarea)
#
#     helper = FormHelper()
#     helper.layout = Layout(
#     # Fieldset('text_input', css_class='form-control-lg'),)
#     class Meta:
#             # specify model to be used
#             model = Post
#
#
#             # specify fields to be used
#             fields = [
#                 "author",
#             ]


class MessageForm(forms.Form):
    title = forms.CharField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.form_show_labels = True
        super().__init__(*args, **kwargs)
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Row('title', css_class='form-control-lg'),
        )
