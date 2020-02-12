from django.shortcuts import render, redirect
from django.forms import formset_factory

from .models import *
from .forms import *

# Create your views here.

def index(request):
	BaseFormSet=formset_factory(BaseForm)

	if request.method == 'POST':

		formset= BaseFormSet(request.POST)

		if formset.is_valid():
			for form in formset:
				form.save()
			return redirect('/result')

	else:

		formset= BaseFormSet()	

	return render(request, 'ask42app/index.html', context={'formset' : formset })


def result(request):
	elements=Data_jsonb.objects.all()

	# print(Data_jsonb.objects.filter(some_element__contains={'owner':'Roman'}))

	return render(request, 'ask42app/result.html', context={'elements' : elements})


