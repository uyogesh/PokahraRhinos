from django.forms import ModelForm
from django import forms
from models import RegistrationFormModel
from django.contrib.admin.widgets import AdminDateWidget


class DateInput(forms.DateInput):
    input_type = 'date'


class RegistrationForm(ModelForm):

    def clean_middle_name(self):
        return self.cleaned_data['middle_name'] or None

    def clean_club_name(self):
        return self.cleaned_data['club_name'] or None

    def clean_other_details(self):
        return self.cleaned_data['other_details'] or None

    class Meta:
        model = RegistrationFormModel
        fields = ['first_name',
                  'middle_name',
                  'last_name',
                  'dob',
                  'citizenship_no',
                  'place_of_issue',
                  'mobile_no',
                  'residential_add',
                  'email',
                  'sex',
                  'height',
                  'weight',
                  'played_for',
                  'bowling_arm',
                  'bowling_pace',
                  'wicket_keeper',
                  'club_name',
                  'batting',
                  'first_preference',
                  'team_captain_experience',
                  'health_issues',
                  'other_details',]
        widgets = {
            'dob': DateInput(),
        }




