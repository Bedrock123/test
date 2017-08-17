from django import forms
from django.contrib.auth import get_user_model
from datetime import datetime
from dateutil.parser import parse
User = get_user_model()


class MemberFormPersonal(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'are_you_a_health_care_prof',
            'date_of_birth',
            'gender',
            'are_you_over_the_age_of_18'
        ]

    def __init__(self, *args, **kwargs):
        super(MemberFormPersonal, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs\
            .update({
                'placeholder': 'First Name',
                'class': 'input-calss_name'
            })
        self.fields['last_name'].widget.attrs\
            .update({
                'placeholder': 'Last Name',
                'class': 'input-calss_name'
            })
        self.fields['phone_number'].widget.attrs\
            .update({
                'placeholder': 'Ex: (555) 555 5555',
                'class': 'input-calss_name'
            })
        self.fields['date_of_birth'].widget.attrs\
            .update({
                'placeholder': 'Ex: MM/DD/YYYY',
                'class': 'input-calss_name'
            })
    def clean(self):
        are_you_over_the_age_of_18 = self.cleaned_data.get('are_you_over_the_age_of_18')
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if are_you_over_the_age_of_18 == 'No':
            if not self._errors.has_key('are_you_over_the_age_of_18'):
                from django.forms.utils import ErrorList
                self._errors['are_you_over_the_age_of_18'] = ErrorList()
                self._errors['date_of_birth'] = ErrorList()
            self._errors['date_of_birth'].append('Sorry, you must be over the age of 18 to user Harper.')
            self._errors['are_you_over_the_age_of_18'].append('Sorry, you must be over the age of 18 to user Harper.')
        return self.cleaned_data


class MemberProfilePhotoForm(forms.ModelForm):
    image_errors = {
        'required': 'Please upload a profile image.',
    }

    profile_image = forms.ImageField(
        label='Select An Image',
        error_messages=image_errors

    )

    class Meta:
        model = User
        fields = [
            'profile_image',

        ]

    def __init__(self, *args, **kwargs):
        super(MemberProfilePhotoForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True


class AllauthSignupForm(forms.Form):

    def signup(self, request, user):
        pass


class MemberFormSetUpPatient(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'how_many_doctor_visits_week',
            'how_many_doctor_visits_month',
            'how_many_doctor_visits_year',
            'email_notifications',
            'how_did_you_hear_about_us'
        ]


class MemberFormSetUpDoctor(forms.ModelForm):

    class Meta:
        model = User
        fields = [
        
            'what_medical_type_are_you',
            'what_health_care_type',
            'email_notifications',
            'how_did_you_hear_about_us'
        ]

    def __init__(self, *args, **kwargs):
        super(MemberFormSetUpDoctor, self).__init__(*args, **kwargs)
        self.fields['what_health_care_type'].widget.attrs\
            .update({
                'placeholder': 'Ex: Oncology',
                'class': 'input-calss_name'
            })
        self.fields['what_health_care_type'].required = True
