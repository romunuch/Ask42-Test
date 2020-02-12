from django import forms

import json

from .models import *



class BaseForm(forms.Form):
	element=forms.CharField()

	element.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter JSON Element'})

	def save(self):
		try:
			json_element=json.loads(self.cleaned_data['element'])
		except:
			raise forms.ValidationError("Invalid data, it must be JSON")

		new_element=Data_jsonb.objects.create(some_element=json_element)

		return new_element

