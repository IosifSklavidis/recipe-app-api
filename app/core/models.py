from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        # if there are any extra fields, it passes in the extra_fields
        # creates and saves a new user
        # normalize_email is a help-fuction from BaseUserManager
        # in order to adjust in the right terms the email
        if not email:
            # insert validation with the if, check the test
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        # creates and saves a new superuser
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    # custom user model that supports using email instead of username
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # assign user manager to object attribute
    objects = UserManager()

    USERNAME_FIELD = 'email'
