from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Blog(models.Model):
	id = models.IntegerField(primary_key=True, editable=False)
	admin = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	posted_date = models.DateField(blank=True, null=True)
	feature_image = models.ImageField(null=True, blank=True)
	blog_image = models.ImageField(null=True, blank=True)
	slug = models.SlugField(unique=True)
	description = models.TextField(null=True, blank=True)


	def __str__(self):
		return str(self.title) + ' | ' + str(self.admin)

	class Meta:
		unique_together = ('title', 'slug')
		ordering = ['-posted_date']

	def get_absolute_url(self):
		return reverse("single",  kwargs={"slug":self.slug})

class UserInfo(models.Model):
	Gender = (
		('Male', 'Male'),
		('Female', 'Female')
		)
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	mobile = models.CharField(max_length=15, null=True, blank=True)
	gender = models.CharField(max_length=6, choices=Gender)
	education = models.CharField(max_length=30, null=True)
	city = models.CharField(max_length=30, null=True)
	country = models.CharField(max_length=30, blank=False)
	profile = models.ImageField(null=True, blank=True)
	Biography = models.TextField(null=True, blank=True)

	def __str__(self):
		return str(self.user)

class Country(models.Model):
	name = models.CharField(max_length=100)
	team_img = models.ImageField(null=True, blank=True)
	flag = models.ImageField(upload_to='country/',blank=False)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return str(self.name)

	class Meta:
		unique_together = ('name', 'slug')

class CountryBlog(models.Model):
	country_post = models.ForeignKey(Country, on_delete=models.CASCADE)
	title = models.CharField(max_length=200, blank=False)
	date = models.DateField()
	slug = models.SlugField(unique=True)
	description = models.TextField()
	feature_img = models.ImageField(null=True, blank=True)
	thumbnail_img = models.ImageField(null=True, blank=True)

	def __str__(self):
		return str(self.title)

	class Meta:
		unique_together = ('title', 'slug')
		ordering = ['-date']

	def get_absolute_url(self):
		return reverse("single",  kwargs={"slug":self.slug})


class CountryPlayers(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	number = models.CharField(max_length=30, blank=True)
	designation = models.CharField(max_length=30)

	def __str__(self):
		return str(self.name)


class CountryMatchStatu(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	match_play = models.CharField(max_length=30, blank=False)
	won = models.CharField(max_length=30, blank=False)
	draw = models.CharField(max_length=30, blank=False)
	lost = models.CharField(max_length=30, blank=False)
	pts = models.CharField(max_length=30, blank=False)

	def __str__(self):
		return str(self.country)



# class FirstVsSecond(models.Model):
# 	first_country = models.CharField(max_length=100, blank=False)
# 	first_country_flag = models.ImageField(upload_to='country/',blank=False)
# 	second_country = models.CharField(max_length=100, blank=False)	
# 	second_country_flag = models.ImageField(upload_to='country/',blank=False)
# 	match_date = models.DateField()
# 	local_time = models.DateTimeField()
# 	stadium_city = models.CharField(max_length=30)
# 	group = models.CharField(max_length=30)


	# def __str__(self):
	# 	return str(self.first_country) + ' vs ' +str(self.second_country)
