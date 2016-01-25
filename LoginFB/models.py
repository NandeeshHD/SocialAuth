from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from allauth.socialaccount.models import SocialAccount

import hashlib


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    is_active = models.BooleanField(_('verified'), default=True,
                help_text=_('Designates whether this user should be treated as '
                            'active.'))

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    class Meta:
        db_table = 'user_profile'

    def profile_image_url(self):
        """
        Return the URL for the user's Facebook icon if the user is logged in via Facebook,
        otherwise return the user's Gravatar URL
        """
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')

        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=120&height=120".format(fb_uid[0].uid)

        return "http://www.gravatar.com/avatar/{}?s=120".format(
            hashlib.md5(self.user.email).hexdigest())
        
    def deauthorize(self):
        self.is_active = False

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])