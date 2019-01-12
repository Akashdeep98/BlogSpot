from django.shortcuts import render
from blogPost.forms import  UserCreateForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,TemplateView,ListView,DetailView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blogPost.models import blogs,comments
from braces.views import SelectRelatedMixin
from django.contrib.auth import get_user_model
from django.conf import settings
User=get_user_model()

# Create your views here.

class SignUp(CreateView):
	form_class=UserCreateForm
	success_url=reverse_lazy('login')
	template_name='blogPost/signup.html'



class CreateBlog(LoginRequiredMixin,SelectRelatedMixin,CreateView):
	login_url='login'
	redirect_feild_name='accounts/create'
	fields=('title','description','content')
	model=blogs	
	def form_valid(self,form):
		if self.request.user.is_authenticated():
			self.object=form.save(commit=False)
			self.object.author=self.request.user
			self.object.save()
			return super(CreateBlog,self).form_valid(form)
			

class indexView(ListView):
	context_object_name='blogs'
	model=blogs
	template_name='blogPost/index.html'	

class ViewBlog(DetailView):
	context_object_name='blog'
	model=blogs
	template_name='blogPost/blog.html'

	#@login_required
	#def comment(request):
	#	if request.method=='POST':
	#		form=comments(data=request.POST)
	#			form_obj=form.save(commit=False)
	##			form_obj.blog=self.kwargs['pk']
	#			self.object.save()





class ThanksView(TemplateView):
	template_name='blogPost/thanks.html'
