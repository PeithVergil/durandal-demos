from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    
    def _create(self, username, password):
        new_user = self.model(username=username)
        
        # Hash the raw password.
        new_user.set_password(password)

        new_user.save(using=self._db)
        
        return new_user

    def create_user(self, username, password):
        return self._create(username, password)

    def create_superuser(self, username, password):
        return self._create(username, password)


class User(AbstractBaseUser):
    """
    A custom user model with minimal fields.
    """

    username = models.CharField(_('username'), unique=True, max_length=128)

    USERNAME_FIELD = 'username'

    # Date the user was created.
    date_created = models.DateTimeField(auto_now_add=True)

    # Date the user was updated.
    date_updated = models.DateTimeField(auto_now=True)

    # Date the user was deleted.
    date_deleted = models.DateTimeField(blank=True, null=True)

    # Add the custom user manager.
    objects = UserManager()

    @property
    def email(self):
        return None
    
    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return 'User(id={0}, username={1})'.format(self.id, self.username)