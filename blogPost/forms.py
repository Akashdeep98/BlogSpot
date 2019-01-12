from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from blogPost.models import blogs
from django import forms

class UserCreateForm(UserCreationForm):

	class Meta:
		fields=('username','email','password1','password2')
		model=get_user_model()

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['username'].label='Display Name'
		self.fields['email'].label='Email'
		self.fields['password1'].label='Password'	
		self.fields['password2'].label='Confirm Password'


class Create_Blog_Form(forms.ModelForm):
	class Meta:
		model=blogs
		fields=('title','description','content')

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['title'].label='Title'
		self.fields['description'].label='Description'
		self.fields['content'].label='Content'	

class Comment_Form(forms.ModelForm):
	class Meta:
		model=blogs
		fields=('content',)
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['content'].label='Comment'			