from django import forms
from .models import Profile, Project,Comment

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile','userinterface']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['profile']
class VoteForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['link','description','profile','image','title']    

class NewComment(forms.ModelForm):
   class Meta:
       model=Comment
       fields=['comment_content']