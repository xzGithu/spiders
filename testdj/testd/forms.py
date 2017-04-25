from django import forms


class Mybook(forms.Form):
    name = forms.CharField()
    author = forms.CharField()
    date = forms.CharField()