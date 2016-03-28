from django import forms
from django.contrib.auth.models import User


class ChangePasswordForm(forms.MOdelForm):
	id=forms.CharField(widget=forms.HiddenInput())
	