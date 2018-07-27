import re

from django.conf import settings
from templated_email import send_templated_mail


def parse_email_from_card(card_desc):
    match = re.search(r'[\w\.-]+@[\w\.-]+', card_desc)
    return match.group(0)

def send_approval_email(card_data):
    recipient_email = parse_email_from_card(card_data['desc'])
    name = card_data['name']

    kwargs = dict(
        template_name='approval',
        from_email=settings.SERVER_EMAIL,
        recipient_list=[recipient_email],
        context={ 
            'name': name
        }
    )
    return send_templated_mail(**kwargs)
