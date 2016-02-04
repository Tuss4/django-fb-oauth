from rest_framework import views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from collections import OrderedDict
from .models import FBToken
from .client import FB_CLIENT
from .utils import get_fields_params


class FacebookLoginView(views.APIView):

    permission_classes = (AllowAny, )

    def get(self, request):
        return HttpResponseRedirect(FB_CLIENT.redirect_url)


class FacebookCallbackView(views.APIView):

    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        if not code:
            return Response(
                {'detail': 'You did not authorize us.'}, status=status.HTTP_401_UNAUTHORIZED)
        query = "client_id={0}&redirect_uri={1}&client_secret={2}&code={3}".format(
            settings.FACEBOOK_CLIENT_ID, FB_CLIENT.redirect_url,
            settings.FACEBOOK_CLIENT_SECRET, code
        )
        at = FB_CLIENT.exchange(query)
        profile = FB_CLIENT.get_profile(
            "graph.facebook.com/v2.5/me",
            "fields={0}&access_token={1}".format(get_fields_params(), at))
        try:
            fb = FBToken.objects.get(facebook_id=profile['id'])
            r = OrderedDict()
            r['id'] = fb.user.pk
            r[fb.user.USERNAME_FIELD] = getattr(fb.user, fb.user.USERNAME_FIELD)
            # If the app use DRF's token based authentication add it to the response dict.
            try:
                r['token'] = fb.user.auth_token.key
            except Exception:
                r['token'] = None
            return Response(r, status=status.HTTP_200_OK)
        except FBToken.DoesNotExist:
            user_kwargs = {pf: profile.get(pf) for pf in settings.FACEBOOK_PROFILE_FIELDS}
            u = FBToken.objects.create_fb_user(profile['id'], at, **user_kwargs)
            r = OrderedDict()
            r['id'] = u.pk
            r[u.USERNAME_FIELD] = getattr(u, u.USERNAME_FIELD)
            # If the app use DRF's token based authentication add it to the response dict.
            try:
                r['token'] = u.auth_token.key
            except Exception:
                r['token'] = None
            return Response(r, status=status.HTTP_201_CREATED)
