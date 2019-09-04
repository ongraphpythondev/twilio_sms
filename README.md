# Twilio

Twilio enables phones, VoIP, and messaging to be embedded into web, desktop, and mobile software.

This application uses django-twilio to send messages.

## Prerequisites:

You will need the following programmes properly installed on your computer.

* [Python](https://www.python.org/) 3.6+
* [Virtual Environment](https://pypi.org/project/virtualenv/)

To install virtual environment on your system use:

```bash
pip install virtualenv

or

pip3 install virtualenv #if using linux(for python 3 and above)
```
* Twilio Account SID
* Twilio Auth Token
* Twilio Phone Number


To get the message application to work you would need to [create](https://www.twilio.com/docs/sms#get-started) an Account on twilio to get the required data.
## Installation:

```bash
git clone https://github.com/ongraphpythondev/twilio_sms.git

cd twilio_sms

virtualenv venv
      or
virtualenv venv -p python3 #if using linux(for python 3 and above)

venv\Scripts\activate # for windows
      or
source venv/bin/activate # for linux

# install required packages for the project to run
pip install -r requirements.txt
```
In Project directory's twilio_sms/settings.py file you would need to change

```python
TWILIO_ACCOUNT_SID = '<account SID provided by twilio>'
TWILIO_AUTH_TOKEN = '<Auth Token provided by twilio>'
TWILIO_PHONE_NUMBER= '<phone number provided by twilio>'
```


## Running:

To run the development server after installation:
```bash
# activate the virtual environment
venv\Scripts\activate # for windows
      or
source venv/bin/activate # for linux

# run server
python manage.py runserver
```
