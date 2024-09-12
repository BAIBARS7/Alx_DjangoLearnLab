from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from .models import Tag
from taggit.forms import TagField, TagWidget  # Import TagWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    tags = TagField(widget=TagWidget(), required=False)  # Use TagWidget here

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include tags in the fields

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content or content.isspace():
            raise forms.ValidationError("Comment cannot be empty")
        return content
