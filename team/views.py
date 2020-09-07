from django.shortcuts import render
from app.models import Team
# Create your views here.

def teamhome(request):
	team = Team.objects.all()
	context = {'teams': team }
	template = 'team/country.html'
	return render(request, template, context)