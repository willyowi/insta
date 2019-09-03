from django import forms
from django.forms import ModelForm, Textarea
from .models import Post,Comment,Profile

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

    # new post form
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['profile'] 


class VoteForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['link','description','profile','image','title']    

class NewComment(forms.ModelForm):
   class Meta:
       model = Comment
       fields=['comment_content']               