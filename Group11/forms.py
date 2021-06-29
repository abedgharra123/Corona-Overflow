# type: ignore
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput,SelectMultiple

from users.models import user

from room.models import room

from blog.models import answer
from blog.models import blog



class RoomModelForm(forms.ModelForm):
    students= forms.ModelMultipleChoiceField(queryset=None)
    class Meta:
        model = room
        fields = ['name','students']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Choose a name','class': 'form-control input-text'}),
        }


    def __init__ (self,u,  *args, **kwargs):
        super(RoomModelForm, self).__init__(*args, **kwargs)
        self.fields["students"].widget = forms.widgets.CheckboxSelectMultiple(attrs={'class':'lst'})
        self.fields["students"].help_text = "These sudents matches your subject!"
        self.fields["students"].queryset = user.objects.filter(is_teacher=False,subject=u.subject)





class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control input-text'})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control input-text'})
    

    class Meta:
        model = user
        fields = ['email','username','password1','password2','subject','is_teacher']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control input-text','placeholder': 'Email Adress'}),
            'username': forms.TextInput(attrs={'class': 'form-control input-text','placeholder': 'Username'}),
            'is_teacher': forms.CheckboxInput(attrs={'class': 'checkbx'}),
            'subject': forms.Select(attrs={'class': 'form-control input-text'}),
        }
        

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['question']
        widgets = {
            'question': forms.Textarea(attrs={'class': 'form-control input-text','placeholder': 'Your Question','rows':4}),
        }


class AnswerModelForm(forms.ModelForm):
    class Meta:
        model = answer
        fields = ['answer']
        widgets = {
            'answer': forms.TextInput(attrs={'class': 'form-control input-text answer','placeholder': 'Add a comment'}),
        }