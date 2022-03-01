from django import forms
from main.models import FeedBack, BookPoint


class ContactForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'


class BookPointForm(forms.ModelForm):
    class Meta:
        model = BookPoint
        fields = '__all__'
