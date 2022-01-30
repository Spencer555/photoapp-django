from django import forms 
from photos.models import Photo


class PhotoForm(forms.ModelForm):
    
    class Meta:
        model = Photo 
        fields = ('image', 'name')


        widgets ={
            'image':forms.FileInput(attrs={'class':'form-control rounded-4'}),
            'name': forms.TextInput(attrs:={'class':'form-control rounded-4', 'placeholder':'Name'})
        }




