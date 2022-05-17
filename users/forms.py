from .models import User
from django.forms import ModelForm


class RegistrantForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'kites_id',
            'name',
            'username',
            'password'
            'email',
            'contact_number',
            'whatsapp_number',
            'state_current',
            'district_current',
            'qualification',
            'occupation',
            'area_of_interest',
            'gender',
            'date_of_birth',
            'current_address',
            'permanent_address',
            'blood_group',
            'skills_endorsements',
            'previous_volunteering_experience',
            'achievements',
            'why_kites',
            'why_contribute_community',
            'profile_image',
            'subject',
            'status_text',
            'tshirt_size',
            'state_permanent',
            'district_permanent'
        ]
