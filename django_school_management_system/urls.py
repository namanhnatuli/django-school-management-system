"""django_school_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordChangeView, PasswordResetDoneView, PasswordResetConfirmView
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

from dashboard.forms import ResetPasswordForm, PasswordChangeForm, SetPasswordForm
from dashboard.views import registeruser, editprofile, loginrequest

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", loginrequest, name="loginrequest"),
    path("register/", registeruser, name="register"),
    path('editprofile/', editprofile, name='editprofile'),
    path('changepassword/', PasswordChangeView.as_view(template_name='registration/changepassword.html', form_class=PasswordChangeForm, success_url=reverse_lazy('dashboard:dashboard')), name='changepassword'),
    path('passwordreset/', PasswordResetView.as_view(template_name='registration/resetpassword.html', form_class=ResetPasswordForm, success_url=reverse_lazy('passwordresetsendmail')), name='resetpassword'),
    path('passwordresetmail/', PasswordResetDoneView.as_view(template_name='registration/sendmailnoti.html'), name='passwordresetsendmail'),
    path('setnewpassword/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/setnewpassword.html', form_class=SetPasswordForm, success_url=reverse_lazy('password_reset_complete')), name='setnewpassword'),

    path('results/', include('result.urls')),
    path('subjects/', include('subjects.urls')),
    path('students/', include('student.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('classes/', include('classes.urls')),
    path('teachers/', include('teachers.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='dashboard/', permanent=True)),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)