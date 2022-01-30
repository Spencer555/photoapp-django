from django import forms 
from profiles.models import Profile 



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image' ,'about']

        widgets ={
            'image':forms.FileInput(attrs={'class':'form-control rounded-4'}),

            'about': forms.Textarea(attrs:={'class':'form-control', 'placeholder':'About', 'rows':"10", 'cols':"5"})
        }




