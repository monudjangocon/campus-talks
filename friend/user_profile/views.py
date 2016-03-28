from django.shortcuts import render_to_response,redirect,render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from forms import SignUpForm
from django.contrib.auth.models import User
from models import UserProfile,MemberProfile




def profile_detail(request,profile_id):
	user_pr=UserProfile.objects.get(id=profile_id)
	member_detail=user_pr.memberprofile_set.all()
	return render_to_response('profile_detail.html',{'user_pr':user_pr,'member_detail':member_detail})



def members(request):
	user_pr=MemberProfile.objects.all()
	return render_to_response('member.html',{'user_pr':user_pr})	


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'account/signup.html', {'form': form})
        else:
		    username = form.cleaned_data.get('username')
		    email = form.cleaned_data.get('email')
		    password = form.cleaned_data.get('password')
		    User.objects.create_user(username=username, password=password, email=email)
		    user = authenticate(username=username, password=password)## user has been added to the current session
		    login(request, user)
		    return redirect('/')
    else:
        return render(request, 'account/signup.html', {'form': SignUpForm()})



def Logout(request):
	logout(request)
	return HttpResponseRedirect('/')