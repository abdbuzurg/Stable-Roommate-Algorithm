from django import forms
from . models import Survey
from django.db import models
from . data import CHOICES, SLEEP_TIME, WAKE_TIME

class SurveyCreateForm(forms.ModelForm):



    scale1 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    scale2 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    scale3 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    scale4 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    scale5 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    scale6 = forms.ChoiceField(choices=SLEEP_TIME, widget=forms.RadioSelect)
    scale7 = forms.ChoiceField(choices=WAKE_TIME, widget=forms.RadioSelect)
    scale8 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Survey
        fields = ('full_name', 'email', 'country','campus','gender', 'year',
                  'scale1','scale2','scale3','scale4','scale5','scale6','scale7','scale8',
                  'extra1','extra2','extra3','extra4','extra5','extra6'
        )
