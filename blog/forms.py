from django import forms
from .models import Post

#PostForm: name of form this show that PostForm is one of ModelForm
class PostForm(forms.ModelForm):
    #'specify that Post' model should be used when make a form on Django.
    class Meta:
        model = Post
        #show what will be written on fields. post.title and post.text
        fields = ('title', 'text',)