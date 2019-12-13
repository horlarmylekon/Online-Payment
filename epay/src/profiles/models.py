from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings


class BaseProfile(models.Model):
    OPTIONS = [('Default', '---------'),
               ('ENG', 'Engineering'),
               ('MTH', 'Mathematics'),
               ('ECN', 'Economics'), ]

    LEVELS = [
        ('Default', '---------'),
        ('Part 1', '100 Level'),
        ('Part 2', '200 Level'),
        ('Part 3', '300 Level'),
        ('Part 4', '400 Level'),
        ('Part 5', '500 Level'),
        ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField(
        "Profile picture", upload_to="profile_pics/%Y-%m-%d/", null=True, blank=True
    )
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    date_of_Birth = models.DateField(verbose_name='Date Of Birth', default='1999-12-12')
    phone_number = models.CharField(verbose_name='Contact', max_length=11)
    email_verified = models.BooleanField("Email verified", default=False)

    # academic information about user
    matric_number = models.CharField(verbose_name='Matric Number',max_length=225)
    dep_option = models.CharField(verbose_name='Option',max_length=225, choices=OPTIONS)
    part = models.TextField(verbose_name='Level', choices=LEVELS)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile".format(self.user)
