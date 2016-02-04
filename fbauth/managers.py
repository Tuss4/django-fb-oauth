from django.db import models
from django.contrib.auth import get_user_model


class FBManager(models.Manager):

    """Manager method to create a Facebook User"""

    def create_fb_user(self, fb_id, token, **kwargs):
        user = get_user_model().objects.create_user(**kwargs)
        fbt = self.model(user=user, facebook_id=fb_id, access_token=token)
        fbt.save(using=self._db)
        return user
