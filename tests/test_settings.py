SECRET_KEY = 'super-legit-key'
INSTALLED_APPS = [
    'tests',
    'fbauth'
]
ATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'fbauthdb',
    }
}
ROOT_URLCONF = 'fbauth.urls'
FACEBOOK_SCOPE = ['email']
FACEBOOK_PROFILE_FIELDS = ['email', 'first_name', 'last_name']
FACEBOOK_CLIENT_ID = "LegitClientId"
FACEBOOK_CLIENT_SECRET = "LegitClientSecret"
FACEBOOK_EXCHANGE_URL = "graph.facebook.com/v2.5/oauth/access_token"
CALLBACK_HOST = "https://example.com"
CALLBACK_ENDPOINT = "/fb/callback"
