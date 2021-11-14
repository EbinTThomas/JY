from django.shortcuts import render, redirect

from .forms import CreateUserForm

from django.utils import timezone

def signup(request):
  if request.method == 'POST':
    form = CreateUserForm(request.POST, request.FILES)
    form.start_date = timezone.now()
    if form.is_valid():
      form.save()
      return redirect('users:login')
    else:
      return render(request, 'registration/signup.html',{
        'form': form,
        'error': True,
      })
  else:
    form = CreateUserForm()
    return render(request, 'registration/signup.html',{
      'form': form
    })