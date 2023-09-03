from django import forms 

from .models import Post, Comment, Like


class UserPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'txt', 'is_private']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control my-5'}),
            'txt': forms.Textarea(attrs={'class':'form-control my-5'}),
            'is_private': forms.CheckboxInput(attrs={'class':'form-control my-5'}),
        }


class UserPost(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['txt']
        widgets = {
            'txt': forms.TextInput(attrs={'class':'form-control my-5'}),
        }


class UserPost(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['vote']
        widgets = {
            'vote': forms.NumberInput(attrs={'class':'form-control my-5'}),
        }
