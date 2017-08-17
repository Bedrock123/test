import pytest
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.storage.fallback import FallbackStorage
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.test import RequestFactory
from mixer.backend.django import mixer
from rest_framework.test import APIClient

from ..views import (UserCreateAPIView, UserDetailAPIView, UserListAPIView,
                     edit_profile_information, edit_profile_photo,
                     login_redirect)

pytestmark = pytest.mark.django_db

print UserCreateAPIView
print UserDetailAPIView
print UserListAPIView


class TestLoginRedirect():

    def test_anonymous(self):
        url = reverse('login_redirect')
        req = RequestFactory().get(url)
        req.user = AnonymousUser()
        resp = login_redirect(req)
        assert 'login' in resp.url, 'Should redirect to login'

    def test_logged_in_user(self):
        url = reverse('login_redirect')
        user = mixer.blend('HarperUser.User', is_superuser=True)
        req = RequestFactory().get(url)
        req.user = user
        setattr(req, 'session', 'session')
        messages = FallbackStorage(req)
        setattr(req, '_messages', messages)
        resp = login_redirect(req)
        assert resp.status_code == 302, 'Should be redirect to home page'


class TestEditProfileInformation():

    def test_anonymous(self):
        url = reverse('HarperUser:edit_profile_information')
        req = RequestFactory().get(url)
        req.user = AnonymousUser()
        resp = login_redirect(req)
        assert 'login' in resp.url, 'Should redirect to login'

    # Turned off for now becuse I deleted the uer update area of the applicatios for react
    # def test_edit_profile_information(self):
    #     url = reverse('HarperUser:edit_profile_information')
    #     user = mixer.blend('HarperUser.User', is_superuser=True)
    #     req = RequestFactory().get(url)
    #     req.user = user
    #     setattr(req, 'session', 'session')
    #     messages = FallbackStorage(req)
    #     setattr(req, '_messages', messages)
    #     resp = edit_profile_information(req)
    #     assert resp.status_code == 200, 'Should be directed to page'

    def test_edit_profile_information_post(self):
        url = reverse('HarperUser:edit_profile_information')
        user = mixer.blend('HarperUser.User', is_superuser=True)
        data = {
            'first_name': 'Zachary',
            'last_name': 'Bedrosian',
            # Need email or form would raise null error
            'email': 'zacharybedrosian@gmail.com'
        }
        req = RequestFactory().post(url, data=data)
        req.user = user
        setattr(req, 'session', 'session')
        messages = FallbackStorage(req)
        setattr(req, '_messages', messages)
        resp = edit_profile_information(req)
        assert resp.status_code == 302, 'Should redirect to success view'
        user.refresh_from_db()
        assert user.first_name == 'Zachary', 'Should update the user'


class TestEditProfilePicture():

    def test_anonymous(self):
        url = reverse('HarperUser:edit_profile_photo')
        req = RequestFactory().get(url)
        req.user = AnonymousUser()
        resp = login_redirect(req)
        assert 'login' in resp.url, 'Should redirect to login'

    def test_edit_profile_photo(self):
        url = reverse('HarperUser:edit_profile_photo')
        user = mixer.blend('HarperUser.User', is_superuser=True)
        req = RequestFactory().get(url)
        req.user = user
        setattr(req, 'session', 'session')
        messages = FallbackStorage(req)
        setattr(req, '_messages', messages)
        resp = HttpResponse(edit_profile_photo(req))
        assert resp.status_code == 200, 'Should be directed to page'

    '''
    AWS S3 was broken at this time so I commented out this test. 2/28/2017 4pm
    '''

    def test_edit_profile_photo_post_and_get_profile_image(self):
        url = reverse('HarperUser:edit_profile_photo')
        user = mixer.blend('HarperUser.User', is_superuser=True)
        img = './HarperUser/tests/test.png'
        with open(img, 'rb') as infile:
            req = RequestFactory().post(
                url,
                {'profile_image': infile}
            )
        req.user = user
        setattr(req, 'session', 'session')
        messages = FallbackStorage(req)
        setattr(req, '_messages', messages)
        resp = edit_profile_photo(req)
        assert resp.status_code == 302, 'Should redirect to success view'
        user.refresh_from_db()
        assert len(
            user.profile_image.name) == 42, 'Should update the user image, count len of file name for test.'

        # Assert that the user get profile image call works as well with the uploaded image
        # I cut the image url at .com to ensure any AWS domain will work.
        # I also cut the signature as well to ensure compariablility
        img_url = user.get_profile_image()
        sig_place = img_url.index('?')
        com_place = img_url.index('.com')
        img_url = img_url[com_place + 4:sig_place]
        assert len(
            img_url) == 82, 'Should output user profile url with out aws signature and aws domain'


class TestUserListAPIView():

    def test_anonymous(self):
        url = reverse('UserListAPIView')
        client = APIClient()
        request = client.get(url, format='json')
        assert 'Authentication credentials were not provided.' in request.data[
            'detail'], 'Should say that login credentials are required'

    def test_logged_in_superuser(self):
        url = reverse('UserListAPIView')
        user = mixer.blend('HarperUser.User', is_superuser=True)
        user2 = mixer.blend('HarperUser.User', is_superuser=False)
        print user2
        client = APIClient()
        client.force_authenticate(user=user)
        request = client.get(url, format='json')
        assert '2' in str(
            request.data["count"]), 'Should indicate a count of 2 (Include both users)'

    def test_logged_in_non_superuser(self):
        url = reverse('UserListAPIView')
        user = mixer.blend('HarperUser.User', is_superuser=False)
        user2 = mixer.blend('HarperUser.User', is_superuser=False)
        print user2
        client = APIClient()
        client.force_authenticate(user=user)
        request = client.get(url, format='json')
        assert '1' in str(request.data[
                          "count"]), 'Should indicate a count of 1 (Include only the requesting user)'


class TestUserDetailAPIView():

    def test_anonymous(self):
        user = mixer.blend('HarperUser.User', is_superuser=True)
        url = reverse('UserDetailAPIView', kwargs={
                      'random_user_id': user.random_user_id})
        client = APIClient()
        request = client.get(url, format='json')
        assert 'Authentication credentials were not provided.' in request.data[
            'detail'], 'Should say that login credentials are required'

    def test_logged_in_superuser_accessing_own_information(self):
        user = mixer.blend('HarperUser.User',
                           is_superuser=True, username='Zach')
        url = reverse('UserDetailAPIView', kwargs={
                      'random_user_id': user.random_user_id})
        client = APIClient()
        client.force_authenticate(user=user)
        request = client.get(url, format='json')
        assert 'Zach' in request.data['username'], 'Should be able to access \
            their own information as superuser'

    def test_logged_in_superuser_accessing_other_user_information(self):
        user = mixer.blend('HarperUser.User', is_superuser=True)
        user2 = mixer.blend('HarperUser.User',
                            is_superuser=False, username='otherUser')
        url = reverse('UserDetailAPIView', kwargs={
                      'random_user_id': user2.random_user_id})
        client = APIClient()
        client.force_authenticate(user=user)
        request = client.get(url, format='json')
        assert 'otherUser' in request.data["username"], 'As a superuser, \
            they should be able to access other users information'

    def test_logged_in_user_accessing_other_user_information(self):
        user = mixer.blend('HarperUser.User',
                           is_superuser=True, username='superUser')
        user2 = mixer.blend('HarperUser.User',
                            is_superuser=False, username='otherUser')
        url = reverse('UserDetailAPIView', kwargs={
                      'random_user_id': user.random_user_id})
        client = APIClient()
        client.force_authenticate(user=user2)
        request = client.get(url, format='json')
        assert 'Sorry' in request.data[
            "detail"], 'Normal users cannot acccess other users inforamtion'

    def test_logged_in_superuser_updating_other_user_information(self):
        user = mixer.blend('HarperUser.User', is_superuser=True)
        user2 = mixer.blend('HarperUser.User',
                            is_superuser=False, username='otherUser')
        url = reverse('UserDetailAPIView', kwargs={
                      'random_user_id': user2.random_user_id})
        client = APIClient()
        client.force_authenticate(user=user)
        data = {
            'first_name': 'Zachary',
            'last_name': 'Bedrosian',
            'email': 'zacharybedrosian@gamil.com'
        }
        request = client.put(url, data, format='json')
        assert 'Zachary' in request.data['first_name'], 'As a superuser, they \
            should be able to update other users infomration'

    def test_logged_in_superuser_deleting_other_user_information(self):
        user = mixer.blend('HarperUser.User', is_superuser=True)
        user2 = mixer.blend(
            'HarperUser.User',
            is_superuser=False,
            username='otherUser'
        )
        url = reverse(
            'UserDetailAPIView',
            kwargs={
                'random_user_id': user2.random_user_id
            }
        )
        client = APIClient()
        client.force_authenticate(user=user)
        request = client.delete(url, format='json')
        print request
        request2 = client.get(url, format='json')
        assert '404' in str(request2.status_code), 'As a superuser, they \
            should be able to delete other users infomration'

    def test_logged_in_user_deleting_own_profile(self):
        user = mixer.blend(
            'HarperUser.User',
            is_superuser=False,
            username='otherUser'
        )
        url = reverse(
            'UserDetailAPIView',
            kwargs={
                'random_user_id': user.random_user_id
            }
        )
        client = APIClient()
        client.force_authenticate(user=user)
        request = client.delete(url, format='json')
        assert 'Sorry, you must be an admin to otherusers.' in request.data[
            'detail'], 'Non superusers cannot delete their own profile'


class TestUserCreateAPIView():

    def test_anonymous(self):
        url = reverse('UserCreateAPIView')
        client = APIClient()
        request = client.get(url, format='json')
        assert 'Authentication credentials were not provided.' in request.data[
            'detail'], 'Should say that login credentials are required'

    def test_logged_in_superuser(self):
        user = mixer.blend(
            'HarperUser.User',
            is_superuser=True,
            username='Zach'
        )
        url = reverse('UserCreateAPIView')
        client = APIClient()
        client.force_authenticate(user=user)
        data = {
            'username': 'new_user',
            'first_name': 'Zachary',
            'last_name': 'Bedrosian',
            'email': 'zbedrosian@gmail.com',
            'password': 'Bedrock123',
            'confirm_password': 'Bedrock123'
        }
        request = client.post(url, data, format='json')
        assert 'new_user' in request.data['username'], 'Should be able to \
            create other users as superuser'

    def test_logged_in_superuser_mismatch_passwords(self):
        user = mixer.blend(
            'HarperUser.User',
            is_superuser=True,
            username='Zach'
        )
        url = reverse('UserCreateAPIView')
        client = APIClient()
        client.force_authenticate(user=user)
        data = {
            'username': 'new_user',
            'first_name': 'Zachary',
            'last_name': 'Bedrosian',
            'email': 'zbedrosian@gmail.com',
            'password': 'Bedrock123',
            'confirm_password': 'Bedrock1234'
        }
        request = client.post(url, data, format='json')
        assert 'this field should match confirm password' in request.data[
            'password'], 'Passwords have to match'

    def test_logged_in_non_superuser(self):
        user = mixer.blend('HarperUser.User',
                           is_superuser=False, username='Zach')
        url = reverse('UserCreateAPIView')
        client = APIClient()
        client.force_authenticate(user=user)
        data = {
            'username': 'new_user',
            'first_name': 'Zachary',
            'last_name': 'Bedrosian',
            'email': 'zbedrosian@gmail.com'
        }
        request = client.post(url, data, format='json')
        assert 'Sorry, you must be an admin to create new users.' in \
            request.data['detail'], 'Should not be able to create other \
                users as non superuser'


class TestLoggedInUserAPIView():

    def test_anonymous(self):
        user = mixer.blend('HarperUser.User', is_superuser=True)
        print user
        url = reverse('LoggedInUserAPIView')
        client = APIClient()
        request = client.get(url, format='json')
        assert 'Authentication credentials were not provided.' in request.data[
            'detail'], 'Should say that login credentials are required'

    def test_logged_in_user_accessing(self):
        user = mixer.blend('HarperUser.User',
                           is_superuser=True, username='Zach')
        url = reverse('LoggedInUserAPIView')
        client = APIClient()
        client.force_authenticate(user=user)
        request = client.get(url, format='json')
        assert 'Zach' in request.data['username'], 'Should be able to access \
            their own information as superuser'
