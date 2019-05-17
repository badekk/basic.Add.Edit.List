from django import forms
from django.utils import timezone
from .models import Patients


class PatientsForm(forms.ModelForm):
    name = forms.CharField(max_length=20, label="First Name")
    surname = forms.CharField(max_length=20, label="Surname")
    pesel = forms.CharField(label="PESEL", min_length=11, max_length=11, widget=forms.NumberInput)
    date_now = forms.DateTimeField(label="Admission Date", initial=timezone.now)

    class Meta:
        model = Patients
        fields = [
            'name',
            'surname',
            'pesel',
            'info',
        ]


class PatientsEditForm(PatientsForm):
    date_now = forms.DateTimeField(label="Admission Date")

    class Meta:
        model = Patients
        fields = [
            'name',
            'surname',
            'pesel',
            'info',
            'date_now',

        ]