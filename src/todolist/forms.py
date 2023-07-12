from django import forms
from .models import *
from django.contrib.auth.hashers import make_password


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        error_messages = {
            'username': {
                'required': ',وارد کردن نام کاربری الزامی است.',
                'invalid': 'نام کاربری معتبر نمی باشد.',
                'unique': 'این نام کاربری قبلا ثبت شده است.',
            },
            'email': {
                'required': ',وارد کردن ایمیل الزامی است.',
                'invalid': 'ایمیل وارد شده معتبر نمی باشد.',
                'unique': 'این ایمیل قبلا ثبت شده است.',
                'invalid_email': 'ایمیل وارد شده معتبر نمی باشد.'
            },
            'password': {
                'required': ',وارد کردن کلمه عبور الزامی است.',
                'invalid': 'کلمه عبور معتبر نمی باشد',
            }}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class Loginform(forms.Form):
    username = forms.CharField(error_messages={
        'required': 'وارد کردن این فیلد الزامی است.',
        'invalid': 'نام کاربری یا رمز عبور معتبر نمی باشد'
    })
    password = forms.CharField(error_messages={
        'required': 'وارد کردن این فیلد الزامی است.',
        'invalid': 'نام کاربری یا رمز عبور معتبر نمی باشد'
    })

