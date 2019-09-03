from django.shortcuts import render
from twilio.rest import Client
from django.conf import settings

from twilio_sms.forms import MessageForm


def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            to = str(form.cleaned_data['to'])
            body = form.cleaned_data['body']
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            try:
                twilio_response = client.messages.create(
                    body=body,
                    to=to, from_=settings.TWILIO_PHONE_NUMBER)
                error = False
            except Exception as e:
                error = e
            response = {'to': to, 'body': body, 'error': error}
        else:
            response = {'form': form}
        return render(request, 'index.html', response)
    else:
        form = MessageForm()
        return render(request, 'index.html', {'form': form})
