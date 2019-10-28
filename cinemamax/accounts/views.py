from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
    username = form.cleaned_data.get('username')
    my_password = form.cleaned_data.get('password1')
    user = authenticate(username=username, password=my_password)
    login(request, user)
    return redirect('seslist/index')
  else:
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
