from django import forms
from .models import Comment


class EmailPostForm(forms.Form):  # First way to create a form
    name = forms.CharField(max_length=25)  # == <input type="text">
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)  # <textarea>


class CommentForm(forms.ModelForm):  # Second way, based on the Model
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
