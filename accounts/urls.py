from django.urls import path

from accounts.views import UserRegistrationView, LoginView, LogoutView, PasswordTokenCheckAPIView, RequestPasswordReset, \
    SetNewPasswordAPIView, VerifyEmailView, GoogleSocialAuthView, MyTokenRefreshView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users/registration/', UserRegistrationView.as_view(), name='user-registration'),
    path('users/registration/Google/', GoogleSocialAuthView.as_view(), name='user-registration-google'),
    path('users/login/', LoginView.as_view(), name='user-login'),
    path('users/logout/', LogoutView.as_view(), name='user-logout'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),

    path('users/email-verify/', VerifyEmailView.as_view(), name='user-email-verify'),
    path('request-reset-password/', RequestPasswordReset.as_view(), name='request-password-reset'),
    path('password-reset/<str:uidb64>/<str:token>', PasswordTokenCheckAPIView.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name='password-reset-compplete'),

]
