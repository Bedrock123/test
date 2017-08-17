from ..admin import UserCreationForm
import pytest


@pytest.mark.django_db
class TestUserCreationForml:
    def test_form_no_data(self):
        form = UserCreationForm(data={})
        assert form.is_valid() is False, (
            'Should be invalid if no data is given')

    def test_succesful_form(self):
        form = UserCreationForm(data={})
        data = {
            'first_name': 'Zachary',
            'middle_name': 'Hratch',
            'last_name': 'Bedrosian',
            'email': 'zacharybedrosian@gmail.com',
            'password1': 'Bedrosian123',
            'password2': 'Bedrosian123'
        }
        form = UserCreationForm(data=data)
        form.save()
        assert form.is_valid() is True, 'Should be valid when data is given'

    def test_passwords_dont_match(self):
        data = {
            'first_name': 'Zachary',
            'middle_name': 'Hratch',
            'last_name': 'Bedrosian',
            'email': 'zacharybedrosian@gmail.com',
            'password1': 'Bedrosian123',
            'password2': 'Bedrosian1234'
        }
        form = UserCreationForm(data=data)
        assert form.is_valid() is False, 'Passwords did not match'
