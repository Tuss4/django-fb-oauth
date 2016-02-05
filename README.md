# Django FB Auth

[ ![Codeship Status for Tuss4/django-fb-oauth](https://codeship.com/projects/ea22b680-ae4f-0133-5844-0eeab60c84ba/status?branch=master)](https://codeship.com/projects/132310) [![PyPI version](https://badge.fury.io/py/django-fb-oauth.svg)](https://badge.fury.io/py/django-fb-oauth)

A simple Facebook OAuth 2 implementation in resuable Django app form.

Python (2.7 >)  
Django (1.7 >)

## Quick Start
+ install the package:  
`pip install django-fb-oauth`
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
## Testing

Run `python manage.py test fbauth`
