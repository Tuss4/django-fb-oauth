# FB Auth

A simple Facebook OAuth 2 implementation in resuable Django app form.

## Quick Start

+ Add 'fbauth' to your `INSTALLED_APPS` setting like this:

```python
INSTALLED_APPS = [
    ...
    'fbauth',
]
```

+ Include the fbauth URLconf in your project urls.py like this:

```python
url(r'^fb/', include('fbauth.urls'))
```

+ Run `python manage.py migrate` to create the FBToken model.

+ Add your Facebook settings to `settings.py`:
 + FACEBOOK_CLIENT_ID: The Facebook app's ID.
 + FACEBOOK_CLIENT_SECRET: The Facebook app's secret.
 + FACEBOOK_EXCHANGE_URL: The Facebook access token URL without the protocol. Ex: `graph.facebook.com/v2.5/oauth/access_token`
 + FACEBOOK_SCOPE: An array of the permissions the Facebook app requests. Ex:
 ```python
 FACEBOOK_SCOPE = ["email"]
 ```
 + FACEBOOK_PROFILE_FIELDS: An array of the fields you need when grabbing the user's profile info. Ex:
 ```python
 FACEBOOK_PROFILE_FIELDS = ["email", "first_name", "last_name"]
 ```
 + CALLBACK_HOST: A string representing your API's url. Ex:
 ```python
 CALLBACK_HOST = 'https://example.com'
 ```
 + CALLBACK_ENDPOINT: A string representing the fb auth callback endpoint. Ex:
 ```python
 CALLBACK_ENDPOINT = "/fb/callback"
 ```
