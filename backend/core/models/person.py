from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Person(models.Model):
    TYPES_CHOICES = (
        ('PAST', _('Pastor')),
        ('STAF', _('Church Staff')),
        ('MEMBER', _('Church Member')),
    )
    SEX_CHOICES = (
        ('F', _('Female')),
        ('M', _('Male')),
    )
    MARITAL_STATUS_CHOICES = (
        ('DI', _('Divorced')),
        ('MA', _('Married')),
        ('SI', _('Single')),
        ('WI', _('Widowed')),
    )
    user = models.ForeignKey(User, related_name='person_user', \
                             verbose_name=_('User'), \
                             on_delete=models.SET_NULL, \
                             null=True, blank=True)
    type = models.CharField(verbose_name=_('Type of Person'), max_length=6, \
                            choices=TYPES_CHOICES, null=True, blank=True)
    attendance = models.IntegerField(verbose_name=_('Number of Attendance'), \
                                     default=0)
    alt_name = models.CharField(verbose_name=_('Alternative Name'), \
                                max_length=100, null=True, blank=True)
    sex = models.CharField(verbose_name=_('Sex'), max_length=3, \
                           choices=SEX_CHOICES, null=True, blank=True)
    dob = models.DateField(verbose_name=_('Date of Birth'), \
                           null=True, blank=True)
    marital_status = models.CharField(verbose_name=_('Marital Status'), max_length=2, \
                               choices=MARITAL_STATUS_CHOICES, null=True, blank=True)
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=20, \
                             null=True, blank=True)
    date_accept_christ = models.DateField(verbose_name=_('Date of Accepting Christ'), \
                                          null=True, blank=True)

    def __unicode__(self):
        try:
            return f"{self.user.first_name} {self.user.last_name}"
        except:
            return f"{self.alt_name}"
