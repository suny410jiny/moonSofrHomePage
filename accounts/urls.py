from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy
from django_pydenticon.views import image as pydenticon_image
app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('logout/',views.logout,name="logout"),
    # path('password_change/', auth_views.PasswordChangeView.as_view(
    #     success_url =reverse_lazy('password_change')
    # ), name='password_change'),
    path('password_change/',views.password_change,name='password_change'),
    # /accounts/login/=>j settings.LOGIN_URL
    path('login/', views.login, name="login"),
    path('identicon/image/<path:data>/', pydenticon_image,name="pydenticon_image"),
    path('edit/', views.profile_edit, name="profile_edit"),
]