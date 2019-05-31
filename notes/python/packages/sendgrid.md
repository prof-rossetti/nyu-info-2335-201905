# The `sendgrid` Package

The `sendgrid` package provides some useful emailing capabilities via the [SendGrid Email Delivery Service](https://sendgrid.com/solutions/email-api/). :mailbox_with_mail: :envelope:

Reference:

  + [Source](https://github.com/sendgrid/sendgrid-python)
  + [Package](https://pypi.python.org/pypi/sendgrid)
  + [Example Usage](https://github.com/sendgrid/sendgrid-python/blob/master/examples/helpers/mail/mail_example.py)
  + [Heroku's SendGrid Guide](https://devcenter.heroku.com/articles/sendgrid)
  + [SendGrid Account Types, including Free Tier](https://sendgrid.com/pricing/)
  + [SendGrid Account Signup](https://signup.sendgrid.com/)
  + [Obtaining API Keys](https://app.sendgrid.com/settings/api_keys)

> NOTE: the instructions below are relevant for version 5.6.0 of this package, however newer versions have been released with breaking changes, and this document needs updating (contributions welcome). But you can continue to reference this document as long as you specify the package version to be 5.6.0 during pip installation (see below).

## Installation

Install `sendgrid`, if necessary:

```sh
pip install sendgrid==5.6.0
```

## Setup

First, [sign up for a free account](https://signup.sendgrid.com/), then click the link in a confirmation email to verify your account. Then [create an API Key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions.

To setup the usage example below, store the API Key value in an environment variable called `SENDGRID_API_KEY`. Also set an environment variable called `MY_EMAIL_ADDRESS` to be the email address you just associated with your SendGrid account (e.g. "abc123@gmail.com").

## Usage

Send yourself an email:

```python
import os
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import * # source of Email, Content, Mail, etc.

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

# AUTHENTICATE

sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

# COMPILE REQUEST PARAMETERS (PREPARE THE EMAIL)

from_email = Email(MY_EMAIL_ADDRESS)
to_email = Email(MY_EMAIL_ADDRESS)
subject = "Hello World from the SendGrid Python Library!"
content = Content("text/plain", "Hello, Email!")
mail = Mail(from_email, subject, to_email, content)

# ISSUE REQUEST (SEND EMAIL)

response = sg.client.mail.send.post(request_body=mail.get())

# PARSE RESPONSE

print(response.status_code) #> 202 means success
print(response.body) #> this might be empty. it's ok.
print(response.headers)
```
