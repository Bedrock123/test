import pytest
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.storage.fallback import FallbackStorage
from django.core.urlresolvers import reverse
from django.test import RequestFactory

from mixer.backend.django import mixer

from ..views import api_home

pytestmark = pytest.mark.django_db


class TestApiHome():

    def test_anonymous(self):
        url = reverse('api_home')
        req = RequestFactory().get(url)
        req.user = AnonymousUser()
        resp = api_home(req)
        assert '403' in str(resp.status_code), 'Should redirect to login'

    def test_logged_in_user(self):
        url = reverse('api_home')
        user = mixer.blend('HarperUser.User', is_superuser=True)
        req = RequestFactory().get(url)
        req.user = user
        setattr(req, 'session', 'session')
        messages = FallbackStorage(req)
        setattr(req, '_messages', messages)
        resp = api_home(req)
        assert resp.status_code == 200, 'Should be redirect to home page'
