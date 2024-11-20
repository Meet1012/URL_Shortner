from django import forms

class Create_form(forms.Form):
    url = forms.CharField(max_length=100)
    
class Edit_from(forms.Form):
    shorten_url = forms.CharField(max_length=100)
    url = forms.CharField(max_length=100)
            
class Fetch_form(forms.Form):
    shorten_url = forms.CharField(max_length=100)
    
class Delete_form(forms.Form):
    shorten_url = forms.CharField(max_length=100)