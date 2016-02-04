from unittest import TestCase
from .utils import get_scope_params, get_fields_params
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.core.urlresolvers import reverse
from unittest import mock
from .client import FB_CLIENT
from .models import FBToken
from django.contrib.auth import get_user_model


class OAuthTest(APITestCase):

    fake_profile = {
        "id": "13g1tF4ceb00kID",
        "first_name": "Dude",
        "last_name": "Bro",
        "email": "dude.bro@simpleton.io"
    }
    code = "100PercentLegitCallbackCode"
    fake_atkn = "SUPERREALLEGITINFALLIBLET0K3N"

    def setUp(self):
        self.fb_callback_url = reverse('fb-callback')
        # print(self.fb_callback_url)

    def test_fb_login(self):
        url = reverse('fb-login')
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_302_FOUND)

    def test_oauth_callback(self):
        with mock.patch.object(FB_CLIENT, 'exchange', return_value=self.code) as mock_exchange:
            with mock.patch.object(FB_CLIENT, 'get_profile',
                                   return_value=self.fake_profile) as mock_profile:
                r = self.client.get(self.fb_callback_url, {'code': self.code})
                self.assertEqual(r.status_code, status.HTTP_201_CREATED)
                self.assertTrue(get_user_model().objects.filter(
                    email=self.fake_profile['email'],
                    first_name=self.fake_profile['first_name'],
                    last_name=self.fake_profile['last_name']).exists())
                self.assertTrue(
                    FBToken.objects.filter(facebook_id=self.fake_profile['id']).exists())


class UtilsTest(TestCase):

    def test_param_methods(self):
        self.assertEqual(get_scope_params(), 'email')
        self.assertEqual(get_fields_params(), 'email,first_name,last_name')
