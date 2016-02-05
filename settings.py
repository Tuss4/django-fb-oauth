from django.conf import settings

settings.INSTALLED_APPS += ['fbauth']

settings.configure(
    FACEBOOK_SCOPE=['email'],
    FACEBOOK_PROFILE_FIELDS=['email', 'first_name', 'last_name'],
    FACEBOOK_CLIENT_ID="LegitClientId",
    FACEBOOK_CLIENT_SECRET="LegitClientSecret",
    FACEBOOK_EXHANGE_URL="graph.facebook.com/v2.5/oauth/access_token",
    CALLBACK_HOST="https://example.com",
    CALLBACK_ENDPOINT="/fb/callback"
)
