import os
import random

from django.contrib.auth import get_user_model, authenticate
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()




def register_social_user(provider , user_id, email , name):

    #i decided to not allow user register with their Google  account , the only thing they can do is sign up with this , so maybe i should rename this after
    # lot things to change here

    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():

        if provider == filtered_user_by_email[0].provider:

            registered_user = authenticate(email=email, password=os.environ.get('SOCIAL_SECRET'))

            return {
                'usename': registered_user.username,
                'email': registered_user.email,
                'toknes': registered_user.tokens(),
            }
        else:
            raise AuthenticationFailed("please continue your login using " + filtered_user_by_email[0].auth_provider)


    else:
        raise AuthenticationFailed("No account found. Please register manually.")