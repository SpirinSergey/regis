from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
from main.models import FeedBack, BookPoint
from .forms import ContactForm, BookPointForm


def contacts_forms(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        bookpoint_form = BookPointForm(request.POST)
        if contact_form.is_valid() and 'contact_form_btn' in request.POST:
            FeedBack.objects.create(
                first_name=contact_form.cleaned_data["first_name"],
                last_name=contact_form.cleaned_data["last_name"],
                phone=contact_form.cleaned_data["phone"],
                email=contact_form.cleaned_data["email"],
                agent_type=contact_form.cleaned_data["agent_type"],
            )

            subject = "New request from the site"
            subject_success = "Thank you for your request!"
            context = {
                'user_first_name': contact_form.cleaned_data["first_name"],
                'user_last_name': contact_form.cleaned_data["last_name"],
                'user_phone': contact_form.cleaned_data["phone"],
                'user_email': contact_form.cleaned_data["email"],
                'user_agent_type': contact_form.cleaned_data["agent_type"],
            }
            message_request = render_to_string('main/emails/contact_form.html', context=context)
            message_success = render_to_string('main/emails/message_success.html', context=context)
            send_mail(subject, message_request, settings.EMAIL_HOST_USER, ['sergeys.verarealty@gmail.com'], fail_silently=False, html_message=message_request)
            # send_mail(subject, message_request, settings.EMAIL_HOST_USER, ['FuntekAnita@gmail.com', 'evgenia.verarealty@gmail.com', 'npolyushkin@gmail.com'], fail_silently=False, html_message=message_request)
            send_mail(subject_success, message_success, settings.EMAIL_HOST_USER, [contact_form.cleaned_data["email"]], fail_silently=False, html_message=message_success)

            messages.success(request, 'Thank you for your request! We will shortly contact you.')

        if bookpoint_form.is_valid() and 'bookpoint_form_btn' in request.POST:
            BookPoint.objects.create(
                first_name=contact_form.cleaned_data["first_name"],
                last_name=contact_form.cleaned_data["last_name"],
                phone=bookpoint_form.cleaned_data["phone"],
                email=bookpoint_form.cleaned_data["email"],
                date=bookpoint_form.cleaned_data["date"],
                agent_type=bookpoint_form.cleaned_data["agent_type"],
            )

            subject = "New request from the site"
            subject_success = "Thank you for your request!"
            context = {
                'user_first_name': contact_form.cleaned_data["first_name"],
                'user_last_name': contact_form.cleaned_data["last_name"],
                'user_phone': bookpoint_form.cleaned_data["phone"],
                'user_email': bookpoint_form.cleaned_data["email"],
                'user_agent_type': contact_form.cleaned_data["agent_type"],
                'user_date_time': bookpoint_form.cleaned_data["date"],
            }
            message_request = render_to_string('main/emails/bookpoint_form.html', context=context)
            message_success = render_to_string('main/emails/message_success.html', context=context)
            send_mail(subject, message_request, settings.EMAIL_HOST_USER, ['sergeys.verarealty@gmail.com'], fail_silently=False, html_message=message_request)
            # send_mail(subject, message_request, settings.EMAIL_HOST_USER, ['FuntekAnita@gmail.com', 'evgenia.verarealty@gmail.com', 'npolyushkin@gmail.com'], fail_silently=False, html_message=message_request)
            send_mail(subject_success, message_success, settings.EMAIL_HOST_USER, [bookpoint_form.cleaned_data["email"]], fail_silently=False, html_message=message_success)

            messages.success(request, 'Thank you for your request! We will shortly contact you.')
    else:
        contact_form = ContactForm()
        bookpoint_form = BookPointForm()

    return {'contact_form': contact_form, 'bookpoint_form': bookpoint_form}