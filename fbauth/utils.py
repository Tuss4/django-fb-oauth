from django.conf import settings


# If the params list is > 1, join up all the elements by a comma and return a string.
# If not just return the single element.
def join_params(params):
    if len(params) > 1:
        return ",".join(params)
    return params[0]


# Return the scope params.
def get_scope_params():
    return join_params(settings.FACEBOOK_SCOPE)


# Return the profile fields params.
def get_fields_params():
    return join_params(settings.FACEBOOK_PROFILE_FIELDS)


# Return callback url.
def get_callback_url(url):
    return ''.join([settings.CALLBACK_HOST, url])
