import json
import urllib

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from .models import Comment
from .forms import PublicTicketForm


# def comments(request):
#     if request.method == 'POST':
#         form = PublicTicketForm(request.POST)
#         if form.is_valid():
#
#             ''' Begin reCAPTCHA validation '''
#             recaptcha_response = request.POST.get('g-recaptcha-response')
#             url = 'https://www.google.com/recaptcha/api/siteverify'
#             values = {
#                 'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
#                 'response': recaptcha_response
#             }
#             data = urllib.parse.urlencode(values).encode()
#             req =  urllib.request.Request(url, data=data)
#             response = urllib.request.urlopen(req)
#             result = json.loads(response.read().decode())
#             ''' End reCAPTCHA validation '''
#
#             if result['success']:
#                 form.save()
#                 messages.success(request, 'New comment added with success!')
#             else:
#                 messages.error(request, 'Invalid reCAPTCHA. Please try again.')
#
#             return redirect('comments')
#     else:
#         form = PublicTicketForm()
#
#     return render(request, '/', {'comments': comments_list, 'form': form})