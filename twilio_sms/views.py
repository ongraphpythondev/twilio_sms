from django.shortcuts import render
from twilio.rest import Client
from django.conf import settings


def index(request):
    if request.method == 'GET':
        to = '+111111111'
        body = 'Hello testing twilio in Django'
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        response = client.messages.create(
            body=body,
            to=to, from_=settings.TWILIO_PHONE_NUMBER)
    return render(request, 'index.html')
