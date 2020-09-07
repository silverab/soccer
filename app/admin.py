from django.contrib import admin

from .models import Blog, UserInfo, Country,CountryBlog, CountryPlayers, CountryMatchStatu

class AdminNew(admin.ModelAdmin):
	search_fields = ['title', 'description']
	prepopulated_fields = {'slug': ('title',)}

class CountryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class CountryBlogAdmin(admin.ModelAdmin):
	list_display = ['title','country_post', 'date']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['country_post', 'date']
	readonly_fields = ['country_post']
	class Meta:
		model = CountryBlog

class CountryPlayerAdmin(admin.ModelAdmin):
	list_display = ['name', 'number', 'designation', 'country']
	class Meta:
		model = CountryPlayers

class CountryMatchAdmin(admin.ModelAdmin):
	list_display = ['country', 'match_play', 'won', 'draw', 'lost', 'pts']
	list_filter = ['country', 'won']
	class Meta:
		model = CountryMatchStatu

admin.site.register(Blog, AdminNew)
admin.site.register(UserInfo)
admin.site.register(Country, CountryAdmin)
admin.site.register(CountryBlog, CountryBlogAdmin)
admin.site.register(CountryPlayers, CountryPlayerAdmin)
admin.site.register(CountryMatchStatu, CountryMatchAdmin)