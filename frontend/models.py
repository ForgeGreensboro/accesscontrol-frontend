from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

SIGNOFF_CHOICES = (
    ('SHOP_HEAD', 'Shop Head'),
    ('SOLO', 'Solo Use'),
    ('SUPERVISED', 'Supervised Use'),
    ('NONE', 'Not Approved to use'),
)

class Shop(models.Model):
    name = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.name

class Machine(models.Model):
    requiresSignOff = models.BooleanField()
    macAddress = models.CharField(max_length=15, unique=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.name

class Membership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reservations = models.ManyToManyField(Machine, through='Reservation')
    signoffs = models.ManyToManyField(Machine, through='SignOff', related_name='SignOffs', through_fields=('member', 'machine'))

    def __str__(self):
        return self.user.username

class Reservation(models.Model):
    reservationStart = models.DateTimeField(null=True)
    reservationEnd = models.DateTimeField(null=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(Membership, on_delete=models.CASCADE, null=True)

class SignOff(models.Model):
    signoffType = models.CharField(max_length=15, null=False, choices=SIGNOFF_CHOICES, default='NONE')
    signoffDate = models.DateField(auto_now_add=True)
    member = models.ForeignKey(Membership, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    signOffBy = models.ForeignKey(Membership, on_delete=models.CASCADE, related_name='SignOff')

