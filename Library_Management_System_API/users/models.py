from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Custom User Manager to handle user creation:
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
    Creates and saves a User with the given username, email, and password.

    Args:
        username (str): The username for the user.
        email (str): The email address for the user.
        password (str, optional): The password for the user. Defaults to None.
        extra_fields: Additional fields to include in the user creation.

    Raises:
        ValueError: If the username or email is not provided.

    Returns:
        CustomUser: The created user instance.
        """
        if not username:
            raise ValueError("The username field must be set")
        if not email:
            raise ValueError("The email field must be set")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given username, first name, last name and password.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password, **extra_fields)

# Custom User Model:
class CustomUser (AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_of_membership = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(
        default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']


    objects = CustomUserManager()
