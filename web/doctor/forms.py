from django import forms

from .models import Appointment, DoctorJoin
from .validators import file_size

class AppointmentForm(forms.ModelForm):
    name = forms.CharField(max_length=225, widget=forms.TextInput(attrs={
        'placeholder': 'Name ...'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email ...',
    }))
    date = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={
        'placeholder': 'Select Appoint Date',
        'type': 'date',
        }))
    phone_number = forms.CharField(max_length=15)
    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Problem ...',
        'rows': '6',
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Phone Number ...'
        }))

    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class DoctorJoinForm(forms.ModelForm):
    name = forms.CharField(max_length=225, widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Name ...'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Your Email ...'
    }))
    file_field = forms.FileField(
        validators=[file_size],
        help_text='max. 2 megabytes'
    )

    class Meta:
        model = DoctorJoin
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DoctorJoinForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    