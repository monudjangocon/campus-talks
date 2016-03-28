from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'friend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$','user_profile.views.home'),
    url(r'^register/$','user_profile.views.signup'),
     url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$','user_profile.views.Logout'),
    url(r'^member/(?P<profile_id>[\w-]+)/$','user_profile.views.profile_detail',name="profile_detail"), 
    url(r'^$','user_profile.views.members'), 
     
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

