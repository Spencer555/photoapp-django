from django import forms
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']


        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control rounded-4'}),

            'email': forms.EmailInput(attrs={'class':'form-control rounded-4'})
        }



