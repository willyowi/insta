from django import forms
from django.forms import ModelForm, Textarea
from .models import Article




    # new post form
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }