from django.shortcuts import render

# Create your views here.
class Register(View, BasicViewMixin):

    def get(self, request):
        registeration_form = RegisterUserForm()
        return render(request, "user/register.html", {"categories": self.categories, "form": registeration_form})

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
        return render(request, 'user/register.html', {"categories": self.categories, 'form': form})


class Login(View, BasicViewMixin):
    def get(self, request):
        form = Loginform()
        return render(request, 'user/login.html', {'categories': self.categories, 'form': form})

    def post(self, request):
        form = Loginform(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user:
                login(request, user)
                response = redirect('Home-page')
                request.session['username'] = form.cleaned_data.get('username')
                return response
        return render(request, 'user/login.html', {"categories": self.categories, 'form': form})

    class Logout(View, BasicViewMixin):
        def get(self, request):
            logout(request)
            response = redirect('Home-page')
            response.set_cookie("token", '')
            return response