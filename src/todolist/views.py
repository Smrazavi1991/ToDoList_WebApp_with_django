from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import *
from .models import *


class Home(LoginRequiredMixin, ListView):
    login_url = "/login/"

    def get_queryset(self):
        return Task.objects.get(owner_id=self.request.user.pk)

    template_name = "todolist/user_tasks.html"


class Register(View):

    def get(self, request):
        registeration_form = RegisterUserForm()
        return render(request, "user/register.html", {"form": registeration_form})

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
        return render(request, 'user/register.html', {'form': form})


class Login(View):
    def get(self, request):
        form = Loginform()
        return render(request, 'user/login.html', {'form': form})

    def post(self, request):
        form = Loginform(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user:
                login(request, user)
                response = redirect('Home-page')
                # request.session['username'] = form.cleaned_data.get('username')
                return response
        return render(request, 'user/login.html', {'form': form})

    class Logout(View):
        def get(self, request):
            logout(request)
            return redirect('Home-page')