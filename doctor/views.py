from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from .forms import AppointmentForm, DoctorJoinForm
from .models import Appointment
from .utils import data

# Create your views here.

class HomeView(View):
	template_name = 'doctor/index.html'
	def get(self, request, *args, **kwargs):
		form = AppointmentForm()
		context = {
			'form': form,
		}
		return render(request, self.template_name, context=context)
	def post(self, request, *args, **kwargs):
		form = AppointmentForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			email = form.cleaned_data.get('email')
			date = form.cleaned_data.get('date')
			phone_number = form.cleaned_data.get('phone_number')
			content = form.cleaned_data.get('content')
			subject = 'Appointment Details'
			message = data(
				name=name,
				email=email,
				date=date.date(),
				phone_number=phone_number,
				content=content
			)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [email, ]
			send_mail(subject, message, email_from, recipient_list)
			instance = Appointment.objects.create(
				name=name,
				email=email,
				date=date,
				phone_number=phone_number,
				content=content
			)
			return redirect('/')
		context = {
			'form': form,
		}
		return render(request, self.template_name, context=context)
class BlogView(TemplateView):
	template_name = 'doctor/blog.html'

class ContactView(TemplateView):
	template_name = 'doctor/contact.html'
	def get(self, request, *args, **kwargs):
		form = AppointmentForm()
		context = {
			'form': form,
		}
		return render(request, self.template_name, context=context)
	def post(self, request, *args, **kwargs):
		form = AppointmentForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			email = form.cleaned_data.get('email')
			date = form.cleaned_data.get('date')
			phone_number = form.cleaned_data.get('phone_number')
			content = form.cleaned_data.get('content')
			subject = 'Appointment Details'
			message = data(
				name=name,
				email=email,
				date=date.date(),
				phone_number=phone_number,
				content=content
			)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [email, ]
			send_mail(subject, message, email_from, recipient_list)
			instance = form.save()
			return redirect('/')
		context = {
			'form': form,
		}
		return render(request, self.template_name, context=context)

class DoctorView(View):
	template_name = 'doctor/doctors.html'
	def get(self, request, *args, **kwargs):
		context = {
			'form': DoctorJoinForm()
		}
		return render(request, self.template_name, context=context)
	def post(self, request, *args, **kwargs):
		form = DoctorJoinForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			# file_name = form.cleaned_data.get()
			file_name_form = form.cleaned_data.get('file_field')
			if file_name_form:
				instance.file_field = file_name_form
				instance.save()
				return redirect('/')
			else:
				return redirect('/error/')
		context = {
			'form': form,
		}
		return render(request, self.template_name, context=context)

class FaqView(TemplateView):
	template_name = 'doctor/faq.html'

class GalleryView(TemplateView):
	template_name = 'doctor/gallery.html'

class ServiceView(TemplateView):
	template_name = 'doctor/services.html'