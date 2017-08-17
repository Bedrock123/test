from __future__ import unicode_literals

import re

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _
from versatileimagefield.fields import PPOIField, VersatileImageField


def random_id():
    unique_id = get_random_string(
        length=8, allowed_chars='0123456789')
    return unique_id


def upload_profile_location(instance, filename, *args, **kwargs):
    location = random_id()
    return "media/profile-images/%s/%s" % (location, filename)


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser,
                     first_name, last_name, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=now,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, first_name, last_name,
                    **extra_fields):
        if len(first_name) > 1:
            first_name = first_name[0].upper() + first_name[1:]
        if len(last_name) > 1:
            last_name = last_name[0].upper() + last_name[1:]

        return self._create_user(username, email, password, False, False, first_name, last_name, **extra_fields)

    def create_superuser(self, username, email, password, first_name, last_name):
        user = self._create_user(
            username, email, password, True, True, first_name, last_name)
        user.is_active = True
        user.save(using=self._db)
        return user


GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)

YES_OR_NO = (
    ('No', 'No'),
    ('Yes', 'Yes'),

)

VISITS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8+', '8+'),
)

HEAR_ABOUT_US = (
    ('online', 'Online'),
    ('doctor', 'Doctor'),
    ('patient', 'Patient'),
    ('friend', 'Friend'),
    ('news', 'News'),
)
PROF = (
    ('Nurse', 'Nurse'),
    ('Doctor', 'Doctor'),
    ('Physicians Assistant', 'Physicians Assistant'),
    ('Dentist', 'Dentist'),
    ('Other', 'Other'),
)

NAME_SUFFIX = (  # Used several common name suffixes
    ('CPA', 'CPA'),
    ('Esq', 'Esq.'),
    ('II', 'II'),
    ('III', 'III'),
    ('IV', 'IV'),
    ('JD', 'JD'),
    ('Jr.', 'Jr.'),
    ('M.D.', 'M.D.'),
    ('Ph. D.', 'Ph. D.'),
    ('Sr.', 'Sr.'),

)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        db_index=True,
         default=random_id,
        verbose_name='Username',
        unique=True,
        max_length=255,
        help_text=_(
            'Required. 255 characters or fewer. Letters, numbers and \
            @/./+/-/_ characters'),
        validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                _('Enter a valid username.'),
                _('invalid')
            )
        ]
    )
    email = models.EmailField(
        db_index=True,
        verbose_name='Email',
        unique=True,
        max_length=255
    )
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=60
    )
    middle_name = models.CharField(
        verbose_name='Middle Name',
        max_length=60,
        blank=True
    )
    date_of_birth = models.CharField(
        verbose_name='Date of Birth',
        max_length=60,
        blank=False,
        null=True
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=60
    )
    are_you_a_health_care_prof = models.CharField(
        verbose_name="Are you a healthcare professional?",
        choices=YES_OR_NO,
        blank=False,
        default='No',
        max_length=120,
        null=True,
    )
    profile_image = VersatileImageField(
        'Profile Image',
        upload_to=upload_profile_location,
        ppoi_field='ppoi',
        blank=True,
        null=True,
    )
    user_signup_profile = models.BooleanField(
        'User Signup Profile',
        default=False,
    )
    needs_new_password = models.BooleanField(
        'Needs New Password',
        default=False
    )
    user_signup_set_up = models.BooleanField(
        'User Signup Set Up',
        default=False
    )
    ppoi = PPOIField(
        'Image PPOI',
        default=(0.5, 0.5),
    )
    phone_number = models.CharField(
        blank=False,
        verbose_name='Phone Number',
        max_length=60,
    )
    is_active = models.BooleanField(
        verbose_name='Active User',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='Staff User',
        default=False
    )
    flagged = models.IntegerField(
        verbose_name='Flagged Count',
        default=0
    )
    date_joined = models.DateTimeField(
        verbose_name='Updated At',
        auto_now=True
    )
    gender = models.CharField(
        'Gender',
        max_length=120,
        choices=GENDER,
        blank=False,
        default="",
    )
    suffix = models.CharField(
        'Name Suffix',
        max_length=120,
        blank=True,
        choices=NAME_SUFFIX,
        default="",
    )
    random_user_id = models.CharField(
        'Random User Id',
        editable=True,
        unique=True,
        max_length=120,
        default=random_id

    )
    how_did_you_hear_about_us = models.CharField(
        'How did you hear about us?',
        max_length=120,
        blank=False,
        choices=HEAR_ABOUT_US,
        default="Online",
    )
    email_notifications = models.CharField(
        'Would you like to receive email notifications?',
        max_length=120,
        blank=False,
        choices=YES_OR_NO,
        default="Yes",

    )
    are_you_over_the_age_of_18 = models.CharField(
        'Are you over the age of 18?',
        help_text='By saying yes to this box, you agree electronically that you are 18 or older.',
        max_length=120,
        blank=False,
        choices=YES_OR_NO,
        default="No",

    )
    harperbot_updates = models.CharField(
        'Would you like Harperbot to provide your information and updates?',
        max_length=120,
        blank=False,
        choices=YES_OR_NO,
        default="Yes",

    )
    harper_bot_pop_up = models.CharField(
        'Would you like Harperbot to automatically pop up when it have an update?',
        max_length=120,
        blank=False,
        choices=YES_OR_NO,
        default="Yes",

    )
    patient_email_notifications = models.CharField(
        'Would you like your patients using harper to be able to find you account?',
        max_length=120,
        blank=False,
        choices=YES_OR_NO,
        default="Yes",

    )
    access_level = models.CharField(
        'LEGACY',
        max_length=120,
        blank=False,
    )
    how_many_doctor_visits_week = models.IntegerField(
        'How many medical related visits do you have a week?',
        blank=False,
        default="1",
    )
    how_many_doctor_visits_month = models.IntegerField(
        'How many medical related visits do you have a month?',
        blank=False,
        default="1",
    )
    how_many_doctor_visits_year = models.IntegerField(
        'How many medical related visits do you have a year?',
        blank=False,
        default="1",
    )
    what_health_care_type = models.CharField(
        'What medical field are you in?',
        max_length=120,
        blank=True,
        default=""

    )
    what_medical_type_are_you = models.CharField(
        'What kind of medical professional are you?',
        max_length=120,
        blank=False,
        choices=PROF,
        default='Doctor'
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()

    def __unicode__(self):
        return smart_text(self.first_name + ' ' + self.last_name)

    def needs_to_complete_profile(self):
        if not self.user_signup_profile:
            return True
        else:
            False

    def needs_to_complete_set_up(self):
        if not self.user_signup_set_up:
            return True
        else:
            False

    def get_access_level_display(self):
        return self.access_level

    def get_full_name(self):
        middle_name = ''
        suffix = ''
        if self.middle_name is not None:
            middle_name = ' ' + str(self.middle_name)
        if self.suffix is not None:
            suffix = self.suffix
        full_name = '%s%s %s %s' % (
            self.first_name, middle_name, self.last_name, suffix)
        return full_name.rstrip()

    def get_short_name(self):
        short_name = '%s %s' % (self.first_name, self.last_name)
        return short_name.rstrip()

    def get_profile_image(self):
        try:
            cropped_image = self.profile_image.crop['300x300']
            return cropped_image.url
        except:
            return ''


@receiver(post_delete, sender=User)
def update_site_users_cache(sender, instance, **kwargs):
    cache.clear()


@receiver(post_save, sender=User)
def update_site_users_cache(sender, instance, **kwargs):
    cache.clear()
