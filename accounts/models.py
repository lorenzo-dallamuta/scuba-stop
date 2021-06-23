from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from string import Template

User = get_user_model()


class Profile(models.Model):
    # username, first_name, last_name, email, is_staff, is_active, date_joined
    # clean, get_full_name, get_short_name, email_user
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='profile')

    # address
    street_address = models.CharField(max_length=255)
    zipcode = models.IntegerField(null=True)
    city = models.CharField(max_length=85)

    # TODO: orders
    # TODO: payment methods, coupons
    # TODO: settings, messages
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return Template('$first $last').substitute(
            first=self.user.first_name, last=self.user.last_name).strip()

    @property
    def full_address(self):
        if not (self.street_address and self.zipcode and self.city):
            return ""
        else:
            return Template('street zip city').substitute(
                street=self.street_address, zip=self.zipcode, city=self.city).strip()

    # # attempt to decouple User and Profile for cases like admin users
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

    def __str__(self):
        return self.user.username
