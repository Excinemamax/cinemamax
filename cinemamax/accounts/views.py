from .forms import UserRegistrationForm
from django.shortcuts import render
from maindb.models import Users

def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            unam=user_form.cleaned_data.get('username')
            uid=Users.objects.last().user_id+1
            umail=user_form.cleaned_data.get('email')
            ucard=user_form.cleaned_data.get('card')
            uphone=user_form.cleaned_data.get('phone')
            u=Users(user_id=uid,uname=unam,email=umail,card=ucard,phone=uphone)
            u.save()
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'user_form': user_form})

