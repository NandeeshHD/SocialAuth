from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.models import SocialApp
from .models import UserProfile

import utils


def deauthorize(request):
    if request.method == 'POST':
        authResponse = request.POST.get('authResponse', '')
        signed_request = authResponse['signedRequest']
        secret = SocialApp.objects.filter(provider='facebook')[0].secret
        # decoded data from signed request
        data = utils.parse_signed_request(signed_request, secret)
        # get the user account
        userAccount = SocialAccount.objects.filter(uid=data['user_id'], provider='facebook')[0]
        # set is_active = false in UserProfile
        userProfile = UserProfile.objects.filter(user_id=userAccount.user_id)[0]
        userProfile.deauthorize()