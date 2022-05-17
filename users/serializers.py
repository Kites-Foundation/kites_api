from rest_framework import serializers
from users import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'name', 'email', 'password',
                  'kites_id',
                  'status_text', 'contact_number',
                  'whatsapp_number', 'area_of_interest', 'blood_group', 'qualification',
                  'subject', 'occupation', 'gender', 'date_of_birth', 'current_address',
                  'state_current', 'district_current', 'permanent_address', 'state_permanent',
                  'district_permanent', 'skills_endorsements', 'previous_volunteering_experience',
                  'achievements', 'why_kites', 'why_contribute_community',
                  'profile_image', 'tshirt_size', 'created_on',
                  'updated_on', 'last_login')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
            'email': {
                'style': {
                    'input_type': 'email'
                }
            }
        }

    def create(self, validated_data):
        user = models.User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
