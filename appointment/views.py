from django.shortcuts import render

# Create your views here.
from django.views import generic

from appointment import forms
from appointment.models import Appointment

class CreateAppointment(generic.CreateView):
	form_class = forms.AppointmentForm
	model = Appointment
