from django.urls import path

from accounts.views import UserRegistrationView, LoginView, LogoutView, PasswordTokenCheckAPIView, RequestPasswordReset, \
    SetNewPasswordAPIView, VerifyEmailView, GoogleSocialAuthView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/auth/users/registration/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/auth/users/registration/Google/', GoogleSocialAuthView.as_view(), name='user-registration-google'),
    path('api/auth/users/login/', LoginView.as_view(), name='user-login'),
    path('api/auth/users/logout/', LogoutView.as_view(), name='user-logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/auth/users/email-verify/', VerifyEmailView.as_view(), name='user-email-verify'),
    path('api/request-reset-password/', RequestPasswordReset.as_view(), name='request-password-reset'),
    path('api/password-reset/<str:uidb64>/<str:token>', PasswordTokenCheckAPIView.as_view(), name='password-reset-confirm'),
    path('api/password-reset-complete/', SetNewPasswordAPIView.as_view(), name='password-reset-compplete'),

]
