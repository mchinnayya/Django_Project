from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'mobile', 'query']
        widgets = {
            'query': forms.Textarea(attrs={'rows': 5}),
        }