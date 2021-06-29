from django import forms

from appointment.models import Appointment

from django.utils import timezone

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('user','appointment_date')

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        self.fields['appointment_date'] = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    def clean_appointment_date(self):
        data = self.cleaned_data['appointment_date']
        list_of_appointments = Appointment.objects.filter(appointment_date__exact=data)

        if len(list_of_appointments) > 0:
            raise forms.ValidationError("Ya hay un turno reservado")

        start_time = timezone.now().replace(microsecond=0, second=0, minute=0)
        if data < start_time:
            raise forms.ValidationError("No puede solicitar un turno para esa fecha")


        return data