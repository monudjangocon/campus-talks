from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class UserProfile(models.Model):
	user=models.OneToOneField(User)

	@models.permalink
	def get_absolute_url(self):
		return ('profile_detail', (), { 'profile_id': self.id })

	def __unicode__(self):
		return self.user.username


class MemberProfile(models.Model):
	users=models.ForeignKey(UserProfile,null=True)
	image=models.ImageField(upload_to='ritu')

	def __unicode__(self):
		return str(self.users_id)
	




def create_profile(sender,instance,created,**kwargs):
    if created:
        profile,created=UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_profile,sender=User)


