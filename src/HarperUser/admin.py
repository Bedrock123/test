from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from HarperUser.models import User


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=(
            "Raw passwords are not stored, so there is no way to see "
            "this user's password, but you can change the password "
            "using <a href=\'../password/\'>this form</a>."
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin, ):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    list_display = ["get_full_name", "username", 'email', 'access_level', 'is_staff', 'is_active']
    list_editable = ['access_level']
    list_filter = (
        ('access_level'),
    )
    readonly_fields=('random_user_id',)
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': (
            'email',
            'first_name',
            'middle_name',
            'last_name',
            'suffix',
            'date_of_birth',
            'are_you_a_health_care_prof',
            'profile_image',
            'phone_number',
            'flagged',
            'gender',
            'random_user_id'


        )}),
        ('Harper info', {'fields': (
            'how_did_you_hear_about_us',
            'email_notifications',
            'patient_email_notifications',
            'access_level',
            'needs_new_password',
            'how_many_doctor_visits_week',
            'how_many_doctor_visits_month',
            'how_many_doctor_visits_year',
            'what_health_care_type',
            'what_medical_type_are_you',
        )}),
        ('Site info', {'fields': (
            'username',
            'is_staff',
            'is_active',
            'is_superuser',
            'groups',
            'user_permissions',
            'last_login',
            'user_signup_profile',
            'user_signup_set_up'
        )}),
    )

    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name')}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

# Handles Django Hi Jack
from hijack_admin.admin import HijackUserAdminMixin
admin.site.unregister(User)


class MyCustomUserAdminWithHijackButton(HijackUserAdminMixin, UserAdmin):
    """
    We're subclassing HijackUserAdminMixin to display the hijack button in the admin.
    """
    list_display = UserAdmin.list_display + ['hijack_field', ]
    exclude = ['date_joined']


admin.site.register(User, MyCustomUserAdminWithHijackButton)
