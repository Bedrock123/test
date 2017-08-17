import pytest
from mixer.backend.django import mixer
from HarperUser.models import User, random_id, upload_profile_location
pytestmark = pytest.mark.django_db


class TestUser:
    def test_user_model(self):
        user = mixer.blend(
            'HarperUser.User',
            username="zacharybedrosian",
            email='zacharybedrosian@gmail.com',
            first_name='Zachary',
            last_name='Bedrosian'
        )
        new_user = user
        assert new_user.pk == 1, 'Should save a new user instance'

    def test_user_unicode(self):
        user = mixer.blend(
            'HarperUser.User',
            username="zacharybedrosian",
            email='zacharybedrosian@gmail.com',
            first_name='Zachary',
            last_name='Bedrosian'
        )
        assert unicode(user) == 'Zachary Bedrosian', 'Should output their full name'

    def test_user_get_full_name_w_middlename(self):
        user = mixer.blend(
            'HarperUser.User',
            username="zacharybedrosian",
            email='zacharybedrosian@gmail.com',
            first_name='Zachary',
            middle_name='John',
            last_name='Bedrosian'
        )
        assert user.get_full_name() == 'Zachary John Bedrosian', 'Should output their full name with middle name'

    def test_user_get_full_name_w_middlename_w_suffix(self):
        user = mixer.blend(
            'HarperUser.User',
            username="zacharybedrosian",
            email='zacharybedrosian@gmail.com',
            first_name='Zachary',
            middle_name='John',
            last_name='Bedrosian',
            suffix='III'
        )
        assert user.get_full_name() == 'Zachary John Bedrosian III', 'Should output their full name with middle name \
                                                                    and their name sufffix'

    def test_user_get_full_name_wo_middlename(self):
        user = mixer.blend(
            'HarperUser.User',
            username="zacharybedrosian",
            email='zacharybedrosian@gmail.com',
            first_name='Zachary',
            last_name='Bedrosian'
        )
        assert user.get_full_name() == 'Zachary Bedrosian', 'Should output their full name with middle name'

    def test_user_get_short_name(self):
        user = mixer.blend(
            'HarperUser.User',
            username="zacharybedrosian",
            email='zacharybedrosian@gmail.com',
            first_name='Zachary',
            middle_name='John',
            last_name='Bedrosian'
        )
        assert user.get_short_name() == 'Zachary Bedrosian', 'Should output their full name without middle name'

    def test_user_get_profile_image_no_image(self):
        user = mixer.blend(
            'HarperUser.User',
            username="zacharybedrosian",
            email='zacharybedrosian@gmail.com',
            first_name='Zachary',
            middle_name='John',
            last_name='Bedrosian'
        )
        assert isinstance(user.get_profile_image(), basestring), 'Should output default profiel image'

    def test_create_user(self):
        self.user = User.objects.create_user(
            username="zacharybedrosian",
            email='zacharybedrosian@gmail.com',
            first_name='Zachary',
            last_name='Bedrosian',
            password='Password123'
        )
        assert self.user.get_short_name() == 'Zachary Bedrosian', 'Should output their full name without middle name'

    def test_create_user_with_error(self):
        with pytest.raises(ValueError):
            self.user = User.objects.create_user(
                username=None,
                email='zacharybedrosian@gmail.com',
                first_name='Zachary',
                last_name='Bedrosian',
                password='Password123'
            )

    def test_create_super_user(self):
        self.user = User.objects.create_superuser(
            username="zacharybedrosian",
            email='zacharybedrosian@gmail.com',
            first_name='Zachary',
            last_name='Bedrosian',
            password='Password123'
        )
        assert self.user.get_short_name() == 'Zachary Bedrosian', 'Should output their full name without middle name'

    def test_random_id(self):
        test_id = random_id()
        assert len(test_id) == 12, 'Should be twelve characters long'

    def test_upload_profile_location(self):
        result = upload_profile_location(self, 'profile_image.png')
        random_result_id = result[21:33]
        assert result == 'media/profile-images/' + random_result_id + '/profile_image.png', 'Should upload file.'
