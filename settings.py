from django.conf import settings

settings.INSTALLED_APPS += ['fbauth']

settings.configure(
    FACEBOOK_SCOPE=['email'],
    FACEBOOK_PROFILE_FIELDS=['email', 'first_name', 'last_name']
)
