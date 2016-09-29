from django import forms
from .models import Post
from .models import PostImage
from .models import Comment

from django.forms.models import inlineformset_factory

MAX_IMAGES = 4

PostImageFormSet = inlineformset_factory(
	Post,
	PostImage,
	can_delete=True,

	extra=4,
	fields=['picture']
)




class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title',)

class PostImageForm(forms.ModelForm):
	class Meta:
		model = PostImage

		fields = ('picture',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ( 'text',)
