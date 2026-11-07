from django import forms
from web_app.models import Contact
from captcha.fields import CaptchaField

class NameForm(forms.ModelForm):
    # name = forms.CharField(max_length=250)
    name = 'nashenas'
    email = forms.EmailField()
    subject = forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = "__all__"