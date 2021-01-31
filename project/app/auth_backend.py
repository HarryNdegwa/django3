from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

User = get_user_model()


class EmailAuthBackend(BaseBackend):

    def authenticate(self,request,email=None,password=None):
        try:
            user = User.objects.get(email=email)
            if (check_password(password,user.password)):
                return user
            return None
        except User.DoesNotExist:
            return None


    def get_user(self,user_id):
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None