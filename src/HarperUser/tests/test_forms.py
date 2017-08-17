import pytest

from .. import forms


@pytest.mark.django_db
class TestMemberFormPersonal:

    def test_form(self):
        form = forms.MemberFormPersonal(data={})
        assert form.is_valid() is False, (
            'Should be invalid if no data is given')

        data = {
            'first_name': 'Zachary',
            'middle_name': 'Hratch',
            'last_name': 'Bedrosian',
            'email': 'zacharybedrosian@gmail.com',
        }
        form = forms.MemberFormPersonal(data=data)
        assert form.is_valid() is True, 'Should be valid when data is given'
