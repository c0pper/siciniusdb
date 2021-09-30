from django import forms

class CreateNewPerson(forms.Form):
    fname = forms.CharField(label="Nome", max_length=30)
    lname = forms.CharField(label="Cognome", max_length=30, required=False)
    birth_date = forms.CharField(label="Data di Nascita", max_length=30, required=False)
    phone = forms.CharField(label="Telefono", max_length=30, required=False)
    city = forms.CharField(label="Città", max_length=30, required=False)
    province = forms.CharField(label="Provincia", max_length=2, required=False)
    job = forms.CharField(label="Lavoro", max_length=30, required=False)