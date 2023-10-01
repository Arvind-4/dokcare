from django.views import View
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import AppointmentForm, DoctorJoinForm
from .models import Appointment
from .utils import data

from backend.views import CustomView

# Create your views here.

class HomeView(CustomView):
	template_name = 'doctor/index.html'
	async def get(self, request, *args, **kwargs):
		form = AppointmentForm()
		context = {
			'form': form,
		}
		return render(request, self.template_name, context=context)
	async def post(self, request, *args, **kwargs):
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
class BlogView(CustomView):
	template_name = 'doctor/blog.html'
	context = {}
	async def get(self, request, *args, **kwargs):
		return render(request, self.template_name, context=self.context)

class ContactView(View):
	template_name = 'doctor/contact.html'
	def get(self, request, *args, **kwargs):
		form = AppointmentForm(request.POST or None)
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
			recipient_list = [email,]
			send_mail(
				subject=subject,
				message=message,
				from_email=email_from,
				recipient_list=recipient_list,
				fail_silently=False,
			)
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

class FaqView(CustomView):
	template_name = 'doctor/faq.html'
	context = {}
	async def get(self, request, *args, **kwargs):
		return render(request, self.template_name, context=self.context)

class GalleryView(CustomView):
	template_name = 'doctor/gallery.html'
	context = {}
	async def get(self, request, *args, **kwargs):
		return render(request, self.template_name, context=self.context)

class ServiceView(CustomView):
	template_name = 'doctor/services.html'
	async def get(self, request, *args, **kwargs):
		form = AppointmentForm()
		context = {
			'form': form,
		}
		return render(request, self.template_name, context=context)
	async def post(self, request, *args, **kwargs):
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
	