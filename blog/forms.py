from django import forms
from .models import CommentModel

class SearchForm(forms.Form):
	query = forms.CharField()

class CommentForm(forms.ModelForm):
	class Meta:
		model = CommentModel
		fields = ('name','email','body')

class EmailPostForm(forms.Form):
	name = forms.CharField(max_length = 25)
	email = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(required=False,widget=forms.Textarea)
