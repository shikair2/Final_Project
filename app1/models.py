from django.db import models
from django.utils.translation import gettext as _

class Pet(models.Model):
    name = models.CharField(
            max_length=100,
            help_text=_('Name of Pet'),
    )

    breed = models.CharField(
            max_length=100,
            help_text=_('Breed of pet')
    )

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    SEX_CHOICE = [
        (MALE, _('male')),
        (FEMALE, _('female')),
        (OTHER, _('other')),
    ]

    sex = models.CharField(
            max_length=15,
            help_text=_('sex of pet'),
            choices=SEX_CHOICE,
            default=OTHER,
     )

    birth_date = models.DateField(
        help_text=_('Birth date of pet'),
    )

    vaccinated = models.BooleanField(
        help_text=_('Whether or not pet is vaccinated'),
    )

    profile_image = models.ImageField(
        help_text=_('Profile picture of pet'),
        blank=True,
        upload_to='profiles_images'
    )

    bio = models.TextField(
        blank=True,
    )

    adopt_me_if = models.TextField(
        blank=True,
    )
    
    first_thing_people_notice_about_me = models.TextField(
        blank=True,
    )
    
    friday_night = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.name

class AdoptRequest(models.Model):
    pet = models.ForeignKey(
            'app1.Pet',
            on_delete=models.CASCADE,
    )

    create_ts = models.DateTimeField(
            auto_now_add=True,
    )

    adopter = models.EmailField(
            help_text=_('Email of adopter'),
    )

    def __str__(self):
        return f'{self.adopter} at {self.create_ts}'

# Create your models here.
