from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator


blood_group_choices = (
    ('A Positive', 'A Positive'),
    ('A Negative', 'A Negative'),
    ('B Positive', 'B Positive'),
    ('B Negative', 'B Negative'),
    ('O Positive', 'O Positive'),
    ('O Negative', 'O Negative'),
    ('AB Positive', 'AB Positive'),
    ('AB Negative', 'AB Negative')
)

education_qualification_choices = (
    ('SSLC', 'SSLC'),
    ('Plus Two', 'Plus Two'),
    ('Under Graduate', 'Under Graduate'),
    ('Post Graduate', 'Post Graduate'),
    ('M Phil', 'M Phil'),
    ('Phd', 'Phd')
)

gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Non Binary', 'Non Binary'),
    ('Gender Non-Conforming', 'Gender Non-Conforming'),
    ('Gender Fluid', 'Gender Fluid'),
    ('Gender Queer', 'Gender Queer'),
    ('Agender Two-Spirit', 'Agender Two-Spirit'),
    ('Khawaja Sira', 'Khawaja Sira'),
    ('Hijra', 'Hijra'),
    ('Muxe', 'Muxe'),
    ('Prefer Not to Say', 'Prefer Not to Say'),
    ('Prefer to Self Describe', 'Prefer to Self Describe')
)

states = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
)

area_of_interest = (
    ('Administration', 'Administration'),
    ('Education', 'Education'),
    ('Health', 'Health'),
    ('Environment', 'Environment'),
    ('Media', 'Media'),
    ('Technology', 'Technology'),
    ('Art & Culture', 'Art & Culture')
)

PHONE_NUMBER_REGEX = r"^((\+91|91|0)[\- ]{0,1})?[456789]\d{9}$"


class UsernameValidator(UnicodeUsernameValidator):
    regex = r"^[\w.@+-]+[^.@+_-]$"
    message = "Please enter letters, digits and @ . + - _ only and username should not end with @ . + - or _"


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Email Not Provided')
        if not username:
            raise ValueError('Name Not Provided')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    kites_id = models.CharField(unique=True, verbose_name="Kites ID", blank=True, default="", max_length=6)
    username_validator = UsernameValidator()
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')
    username = models.CharField(max_length=20, verbose_name='Username', unique=True, validators=[username_validator])
    name = models.CharField(max_length=200, verbose_name='Name', default='', blank=True)
    phone_number_regex = RegexValidator(
        PHONE_NUMBER_REGEX,
        message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
        code="invalid_mobile",
    )
    status_text = models.CharField(max_length=250, default='', blank=True)
    contact_number = models.CharField(max_length=10, null=False, validators=[phone_number_regex],
                                      verbose_name='Contact Number')
    whatsapp_number = models.CharField(max_length=10, null=False, validators=[phone_number_regex],
                                       verbose_name='Whatsapp Number')

    area_of_interest = models.CharField(choices=area_of_interest, max_length=20, verbose_name='Area of Interest',
                                        default='', blank=True)

    blood_group = models.CharField(choices=blood_group_choices, max_length=50,
                                   verbose_name='Blood Group', default='', blank=True)
    qualification = models.CharField(default='', blank=True, max_length=100, choices=education_qualification_choices,
                                     verbose_name='Education Qualification')
    subject = models.CharField(max_length=100, default='', verbose_name="Subject ( major )", blank=True)
    occupation = models.CharField(max_length=200, verbose_name='Occupation', default='', blank=True)
    gender = models.CharField(max_length=50, default='', blank=True, choices=gender, verbose_name="Gender")
    date_of_birth = models.DateField(blank=True, verbose_name="Date Of Birth")

    current_address = models.TextField(max_length=200, default='', blank=True, verbose_name="Current Address")
    state_current = models.CharField(max_length=100, choices=states, default='', blank=True,
                                     verbose_name="Current State")
    district_current = models.CharField(max_length=100, verbose_name="Permanent District", blank=True)

    permanent_address = models.TextField(max_length=200, default='', blank=True, verbose_name="Permanent Address")
    state_permanent = models.CharField(max_length=100, choices=states, default='',
                                       blank=True, verbose_name="Permanent State")
    district_permanent = models.CharField(max_length=100, verbose_name="Permanent District", blank=True)

    skills_endorsements = models.TextField(max_length=200, default='', blank=True, verbose_name="Skills & Endorsements")
    previous_volunteering_experience = models.TextField(max_length=200, default='', blank=True,
                                                        verbose_name="Previous Volunteering Experience")
    achievements = models.TextField(max_length=200, default='', blank=True, verbose_name="Achievements")
    why_kites = models.TextField(max_length=200, default='', blank=True, verbose_name="Why Kites ?")
    why_contribute_community = models.TextField(max_length=200, default='', blank=True,
                                                verbose_name="How do you wish to contribute to the community ?")
    profile_image = models.URLField(default='https://cdn.kites.foundation/img/logo.png', blank=True, verbose_name='Profile Image Url')
    tshirt_size = models.CharField(max_length=10, default='', blank=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Users'
