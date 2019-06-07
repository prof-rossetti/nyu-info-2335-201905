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

> NOTE: previous versions of these instructions were applicable for sendgrid package version 5.6.0, but the examples below apply to a more current version (6.0.5)

## Installation

Install `sendgrid`, if necessary:

```sh
pip install sendgrid==6.0.5
```

## Setup

First, [sign up for a free account](https://signup.sendgrid.com/), then click the link in a confirmation email to verify your account. Then [create an API Key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions.

To setup the usage examples below, store the API Key value in an environment variable called `SENDGRID_API_KEY`. Also set an environment variable called `MY_EMAIL_ADDRESS` to be the email address you just associated with your SendGrid account (e.g. "abc123@gmail.com").

## Usage

Send yourself an email:

```py

```

### Using Email Templates

> Thanks to @mgallea for [surfacing](https://github.com/mgallea/daily-email/blob/master/app/main.py) these capabilities

If you'd like further control over the content displayed in the email's body, you can use Sendgrid's email templates.

References:

  + https://sendgrid.com/docs/ui/sending-email/how-to-send-an-email-with-dynamic-transactional-templates/
  + https://sendgrid.com/docs/for-developers/sending-email/using-handlebars/#iterations
  + https://sendgrid.com/dynamic_templates/
  + https://github.com/sendgrid/sendgrid-python/blob/master/USAGE.md#templates


Navigate to __________ and ______________ and store it in an environment variable called `SENDGRID_TEMPLATE_ID`.










Let's try this example email template which represents a grocery receipt:

![](/img/notes/python/packages/sendgrid/receipt.png)












The HTML template used to send this email is:

```html
<img src="https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png">

<h3>Hello this is your receipt</h3>

<p>Date: {{human_friendly_timestamp}}</p>

<p>Total: {{total_price_usd}}</p>

<ul>
{{#each products}}
	<li>You ordered: {{this.name}}</li>
{{/each}}
</ul>

![](/img/notes/python/packages/sendgrid/receipt.png)

We need to pass data to this template. Specifically, this template requires a data structure with attributes called `human_friendly_timestamp`, `total_price_usd`, and a list of `products` each with its own `name` attribute. Something like this dictionary:

```py
{
    "total_price_usd": "$14.95",
    "human_friendly_timestamp": "July 4th, 2019 10:00 AM",
    "products":[
        {"id":1, "name": "Product 1"},
        {"id":2, "name": "Product 2"},
        {"id":3, "name": "Product 3"},
        {"id":2, "name": "Product 2"},
        {"id":1, "name": "Product 1"}
    ]
}
```

We can pass that those attributes when we send the email:

```py

import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID", "OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

SUBJ = "Your Receipt from the Green Grocery Store"

client = SendGridAPIClient(SENDGRID_API_KEY)
print("CLIENT:", type(client)) #> ____________

message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS, subject=SUBJ)
print("MESSAGE:", type(message)) #> ________

message.template_id = SENDGRID_TEMPLATE_ID

message.dynamic_template_data = {
    "total_price_usd": "$14.95",
    "human_friendly_timestamp": "June 1st, 2019 10:00 AM",
    "products":[
        {"id":1, "name": "Product 1"},
        {"id":2, "name": "Product 2"},
        {"id":3, "name": "Product 3"},
        {"id":2, "name": "Product 2"},
        {"id":1, "name": "Product 1"}
    ]
}

try:
    response = client.send(message)
    print("RESPONSE:", type(response))
    print(response.status_code)
    print(response.body)
    print(response.headers)

except Exception as e:
    print("OOPS", e)

```
