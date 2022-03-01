from posts.models import Post
from django.forms import ModelForm, fields

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'