#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from django.contrib.auth.models import User
#from .models import CitizenProfile, UserRole

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        # ينشئ بروفايل مع دور مواطن بشكل تلقائي
#        CitizenProfile.objects.create(user=instance, role=UserRole.CITIZEN)
