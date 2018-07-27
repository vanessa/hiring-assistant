import requests
from decouple import config


class TrelloWrapper:
    def __init__(self):
        self.api_root = 'https://api.trello.com/1'
        self.board_id = config('DEFAULT_BOARD_ID')
        self.done_list_title = config('DEFAULT_DONE_LIST_TITLE')
        self.pending_list_title = config('DEFAULT_PENDING_LIST_TITLE')
        self.default_params = {
            'key': config('TRELLO_KEY'),
            'token': config('TRELLO_TOKEN')
        }

    def _board_request(self, endpoint):
        url = f'{self.api_root}/boards/{self.board_id}/{endpoint}'
        return requests.get(url, params=self.default_params).json()

    def get_list_id_from_title(self, title):
        response = self._board_request('lists')
        list_id = [
            list['id'] for list in response
            if list['name'] == title
        ][0]
        return list_id

    def get_approved_cards_from_list(self):
        pending_list_id = self.get_list_id_from_title(self.pending_list_title)
        response = self._board_request('cards')
        approved_cards = [
            card for card in response
            if card['idList'] == pending_list_id
               and card['labels']  # Check if at least one label exists
               and card['labels'][0]['name'] == 'Approved'
        ]
        return approved_cards

    def move_processed_card_to_done(self, card_id):
        done_list_id = self.get_list_id_from_title(self.done_list_title)
        url = f'{self.api_root}/cards/{card_id}'
        self.default_params['idList'] = done_list_id
        return requests.put(url, params=self.default_params)
