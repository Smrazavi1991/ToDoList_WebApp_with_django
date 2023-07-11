import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True

    is_deleted = models.BooleanField('Is Deleted', default=False)
    last_change = models.DateTimeField('Last Change', auto_now=True, editable=False)
    create_date = models.DateTimeField('Create Date', auto_now_add=True, editable=False)
    delete_datetime = models.DateTimeField('Delete Datetime', default=None, null=True, blank=True, editable=False)


class User(AbstractUser):
    email = models.EmailField('Email Address', unique=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name()


class Task(BaseModel):
    name = models.CharField('Name', max_length=200)
    description = models.CharField('Description', max_length=2000)
    due_date = models.DateTimeField('Due Date')
    done = models.BooleanField('Done', default=False)
