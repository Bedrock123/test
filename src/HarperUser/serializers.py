from rest_framework import serializers

from HarperUser.models import User
from datetime import datetime
from django.utils import formats


class UserCreateSerializer(serializers.ModelSerializer):
    random_user_id = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'random_user_id',
            'password',
            'confirm_password',
            'access_level',
            'phone_number',
            'is_staff',
            'is_superuser',

        ]

    def create(self, validated_data):
        print validated_data
        if validated_data['password'] != validated_data['confirm_password']:
            raise serializers.ValidationError(
                {'password': ['this field should match confirm password']})
        try:
            e_contact_phone_number = validated_data['e_contact_phone_number']
        except:
            e_contact_phone_number = ''
        try:
            e_contact_full_name = validated_data['e_contact_full_name']
        except:
            e_contact_full_name = ''
        try:
            phone_number = validated_data['phone_number']
        except:
            phone_number = ''
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            access_level=validated_data['access_level'],
            avatar_icon=validated_data['avatar_icon'],
            phone_numner=phone_number,
            e_contact_full_name=e_contact_full_name,
            e_contact_phone_number=e_contact_phone_number,
            is_staff=validated_data['is_staff'],
            is_superuser=validated_data['is_superuser'],

        )
        user.set_password(validated_data['password'])
        user.save()

        return user

# Allows us to create a Detail View Url and attach it to the list view


class UserUrlField(serializers.HyperlinkedIdentityField):
    lookup_field = 'random_user_id'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = UserUrlField(view_name='UserDetailAPIView')
    username = serializers.CharField(read_only=True)
    access_level = serializers.SerializerMethodField()
    date_joined = serializers.SerializerMethodField()
    random_user_id = serializers.CharField(read_only=True)
    
    class Meta:
        model = User
        fields = [
            'url',
            'random_user_id',
            'username',
            'email',
            'first_name',
            'middle_name',
            'last_name',
            'access_level',
            'profile_image',
            'needs_new_password',
            'phone_number',
            'is_active',
            'is_staff',
            'is_superuser',
            'gender',
            'date_of_birth',
            'are_you_a_health_care_prof',
            'suffix',
            'date_joined',
            'email_notifications',
            'patient_email_notifications',
            'how_many_doctor_visits_week',
            'how_many_doctor_visits_month',
            'how_many_doctor_visits_year',
            'what_health_care_type',
            'what_medical_type_are_you',
            'harperbot_updates',
            'harper_bot_pop_up',
            'user_signup_profile',
            'user_signup_set_up'


        ]

    def get_access_level(self, obj):
        return obj.get_access_level_display()

    def get_date_joined(self, obj):
        return formats.date_format(obj.date_joined, "SHORT_DATETIME_FORMAT")