from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserInfo

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class UserInfoForm(ModelForm):
	class Meta:
		model = UserInfo
		fields = ('gender', 'mobile', 'education', 'city', 'country', 'profile', 'Biography')

	def __init__(self, *args, **kwargs):
			super(UserInfoForm,self).__init__(*args, **kwargs)
			self.fields['gender'].empty_label = 'Choose'