from django.shortcuts import render

# Create your views here.
from django.views import generic

from appointment import forms
from appointment.models import Appointment

from datetime import date, timedelta

from django.utils import timezone

class CreateAppointment(generic.CreateView):
	form_class = forms.AppointmentForm
	model = Appointment

	def get_context_data(self, **kwargs):
	 	context = super().get_context_data(**kwargs)
	 	all_appointments = Appointment.objects.filter(appointment_date__gt=date.today()).order_by('appointment_date')

	 	start_time = timezone.now().replace(microsecond=0, second=0, minute=0, hour=9)
	 	counter = 0

	 	free_appointments = []

	 	while counter < 5:
	 		free_slot = True
	 		for appointment in all_appointments:
	 			if appointment.appointment_date == start_time:
	 				free_slot = False
	 				break

	 			if appointment.appointment_date > start_time:
	 				break
			
	 		if free_slot:
 				free_appointments.append(start_time)
 				counter += 1

	 		start_time = start_time + timedelta(hours=0.5)

	 	context['free_appointments'] = free_appointments

	 	return context

class ListAppointment(generic.ListView):
	model = Appointment

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.order_by('appointment_date')