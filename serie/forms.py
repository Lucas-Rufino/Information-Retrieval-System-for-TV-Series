from django import forms

class queryForm(forms.Form):
    title = forms.CharField(label = "title",max_length = 200)
    resume = forms.CharField(label = "resume")
    rate = forms.CharField(label = "rate")
    genre = forms.CharField(label ="genre")
    cast = forms.CharField(label="cast")
    general = forms.CharField(label="general")