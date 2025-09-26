from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'accounts/signup.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboards/dashboard_user.html')
