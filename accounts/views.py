from re import template

from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponseRedirect

from accounts.form import SignupForm, ProfileForm, PasswordChangeForm
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, logout_then_login,
    PasswordChangeView as AuthPasswordChangeView
)

from django.contrib.auth import get_user_model, login as auth_login, authenticate

User = get_user_model

# Create your views here.

# login = LoginView.as_view(template_name="accounts/login_form.html")
login = LoginView.as_view(template_name="accounts/login_form.html")
# def login(request):
#     print(request.POST)
#     username = request.POST['username']
#     password = request.POST['password']
#     print(username)
#     print(password)
#     user = auth.authenticate(request, username=username, password=password)
#     print(user)
#     if user is not None:
#         messages.error(request, '로그인에 실패 하셨습니다.')
#         login(request, user)
#         return redirect('/')
#     else:
#         messages.error(request, '로그인에 실패 하셨습니다.')
#         return redirect('accounts/login_form.html')

# logout = LogoutView.as_view()
# logout = LogoutView.as_view(template_name ="accounts/login_form.html")

def logout(request):
    messages.success(request, '로그아웃 되었습니다.')
    auth.logout(request)
    return redirect('/')
    # return logout_then_login('/')


def signup(request):
    print("signup")
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signup_user = form.save()
            auth_login(request, signup_user)
            messages.success(request, "회원가입 환영합니다.")
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()

    return render(request, 'accounts/signup_form.html', {
        'form': form
    })


@login_required
def profile_edit(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid:
            form.save()
            messages.success(request, "프로파일이 수정/저장되었습니다.")
            return redirect("profile_edit")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "accounts/profile_edit_form.html", {
        'form': form,
    })


class PasswordCheangeView(LoginRequiredMixin, AuthPasswordChangeView):
    success_url = reverse_lazy('password_change')
    template_name = "accounts/password_change_form.html"
    form_class = PasswordChangeForm

    def form_valid(self, form):
        messages.success(self.request, "암호를 변경 했습니다.")
        return super().form_valid(form)


password_change = PasswordCheangeView.as_view()