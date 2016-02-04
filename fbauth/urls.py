from django.conf.urls import url
from .api import FacebookLoginView, FacebookCallbackView


urlpatterns = [
    url(r'^login/?$', FacebookLoginView.as_view(), name='fb-login'),
    url(r'^callback/?$', FacebookCallbackView.as_view(), name='fb-callback')
]
