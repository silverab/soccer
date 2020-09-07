from django.shortcuts import render, Http404, redirect, HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import CreateUserForm, UserInfoForm
from app.models import Blog, UserInfo, Country, CountryBlog, CountryMatchStatu, CountryPlayers
from datetime import datetime, timedelta



@login_required
def profile(request):
	user = User.objects.all()
	context = { 'count': user }
	template = 'app/profile.html'
	return render(request, template, context)

@login_required
def delprofile(request):
	user = User.objects.all()
	context = { 'count': user }
	template = 'app/profile.html'
	response = render(request, template, context)
	response.delete_cookie('name')
	return response

def Signup(request):
	if request.method == 'POST':

		form = CreateUserForm(request.POST)
		info_form = UserInfoForm(request.POST, request.FILES)


		if form.is_valid() and info_form.is_valid():
			user =	form.save()
			profile = info_form.save(commit=False)
			profile.user = user
			profile.save()


			# username = form.cleaned_data.get('username')
			# password = form.cleaned_data.get('password1')
			# user = authenticate()
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')

			return redirect('home')
	else:
		# cookie_name = request.COOKIES.get('name', 'Guest') ## get cookie to show in browser
		cookie_name = request.get_singed_cokkie('name', salt='ab')
		form = CreateUserForm()
		info_form = UserInfoForm(request.POST, request.FILES)
		context = {'form': form, 'info_form': info_form, 'cookie_name': cookie_name}
		return render(request, 'registration/signup.html', context)
	
	# return redirect('login')

def home(request):
	news = Blog.objects.all()
	team = CountryMatchStatu.objects.all()
	template = 'app/index.html'
	context = {'news': news, 'teams':team}
	response = render(request, template, context)
	# response.set_cookie('name', 'User', max_age=60*60*24)
	response.set_signed_cookie('name', 'User', salt='ab' , expires=datetime.utcnow()+timedelta(days=2))
	return response

@login_required
def matches(request):
	news = Blog.objects.all()
	template = 'app/matches.html'
	context = {'news': news}
	return render(request, template, context)


@login_required
def teams(request):
	teams = Country.objects.all()
	paginator = Paginator(teams, 8)
	page = request.GET.get('page')
	# ?page=2
	teams = paginator.get_page(page)
	template = 'app/teams.html'
	context = {'teams': teams}
	return render(request, template, context)

@login_required
def country(request, slug):
	news = Blog.objects.all().order_by('-id')[:3]
	paginator = Paginator(news, 3)
	page = request.GET.get('page')
	# ?page=2

	news = paginator.get_page(page)
	

	team = Country.objects.get(slug=slug)
	player = CountryPlayers.objects.all()
	
	template = 'app/single_team.html'
	context = {'team': team, 'news': news, 'players': player}
	return render(request, template, context)
	
	# try:
	# 	team = Country.objects.get(slug=slug)
	# 	template = 'app/single_team.html'
	# 	context = {'team': team}
	# 	return render(request, template, context)
	# except:
	# 	raise Http404
	# return render(request, 'app/single.html')


def blog(request):
	news = Blog.objects.all()
	paginator = Paginator(news, 3)
	page = request.GET.get('page')
	# ?page=2

	news = paginator.get_page(page)
	template = 'app/blog.html'
	context = {'news': news}
	return render(request, template, context)

def single(request, slug):
	try:
		new = Blog.objects.get(slug=slug)
		template = 'app/single.html'
		context = {'new': new}
		return render(request, template, context)
	except:
		raise Http404
	# return render(request, 'app/single.html')



def contact(request):
	return render(request, 'app/contact.html')
