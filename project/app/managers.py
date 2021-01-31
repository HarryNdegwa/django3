from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):

    """
    custom user manager where email is the identifier for authentication instead of username
    """

    def create_user(self,email,password,**extra_fields):
        """
        Create and save a user with given email and password
        """

        if not email:
            raise ValueError(_("Email is required!"))
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self,email,password,**extra_fields):
        """
        create and save a superuser with email and password given
        """

        # this fields do not exist in the extra_fields object
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        self.create_user(email,password,**extra_fields)