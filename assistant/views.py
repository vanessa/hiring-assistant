from django.shortcuts import render
from django.http import HttpResponse
from .helpers.trello import TrelloWrapper
from .helpers.emails import send_approval_email

def index(request):
    trello = TrelloWrapper()
    approved_cards = trello.get_approved_cards_from_list()
    for card in approved_cards:
        send_approval_email(card)
        trello.move_processed_card_to_done(card['id'])
    return HttpResponse('Done!')
