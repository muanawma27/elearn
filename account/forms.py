from django.db.models import fields
from django.forms.models import ModelForm

from .models import *

class ProfessionIkigaiForm(ModelForm):
    class Meta:
        model=UserIkigai
        fields= [
            # 'user',
        'professsion_ikigai1','profession_ikigai1_value',
        'professsion_ikigai2','profession_ikigai2_value',
        'professsion_ikigai3','profession_ikigai3_value',
        'professsion_ikigai4','profession_ikigai4_value',
        'professsion_ikigai5','profession_ikigai5_value',
        ]

class InterestIkigaiForm(ModelForm):
    class Meta:
        model=UserIkigai
        fields= [
            # 'user',
        'interest_ikigai1','interest_ikigai1_value',
        'interest_ikigai2','interest_ikigai2_value',
        'interest_ikigai3','interest_ikigai3_value',
        'interest_ikigai4','interest_ikigai4_value',
        'interest_ikigai5','interest_ikigai5_value',
        ]

class HobbyIkigaiForm(ModelForm):
    class Meta:
        model=UserIkigai
        fields= [
            # 'user',
        'hobby_ikigai1','hobby_ikigai1_value',
        'hobby_ikigai2','hobby_ikigai2_value',
        'hobby_ikigai3','hobby_ikigai3_value',
        'hobby_ikigai4','hobby_ikigai4_value',
        'hobby_ikigai5','hobby_ikigai5_value',
        ]


class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields= '__all__'
