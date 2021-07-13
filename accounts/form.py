from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    PasswordChangeForm as AuthPasswordChangeForm)
from .models import User

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True  # 필수 필드 지정
        self.fields['first_name'].required = True  # 필수 필드 지정
        self.fields['last_name'].required = True  # 필수 필드 지정

        # self.fields['gender'].required = False  # 필수 필드 지정
        # self.fields['phone_number'].required = False  # 필수 필드 지정

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class PasswordChangeForm(AuthPasswordChangeForm):
    # def clean_new_password2(self):
    #     old_passwored = self.cleaned_data.get('old_password')
    #     new_password2= super().clean_new_password2()
    #     if old_passwored == new_password2 :
    #         raise forms.ValidationError("새로운 암호는 기존암호와 다르게 변경 해주세요")
    #     return new_password2

    def clean_new_password1(self):
        old_passwored = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        if old_passwored == new_password1:
            raise forms.ValidationError("새로운 암호는 기존암호와 다르게 변경 해주세요")
        return new_password1
