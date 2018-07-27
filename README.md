# Hiring Assistant
A simple Django project to send automatic e-mails whenever its index URL is called.

On this [example board](https://trello.com/b/rpnspWv1/hiring), there are three columns:
<div style="text-align: center;">
    <img src="https://i.imgur.com/fdVqFhr.png" width="600">
</div>

- Interview phase: Ignored by the script, cards needs to be moved manually to the second column
- **To send-email**: The column used to run the script, defined by env var `DEFAULT_PENDING_LIST_TITLE`
- Done: The column which the script sends the cards that were processed (to avoid e-mails to be sent twice), defined by env var `DEFAULT_DONE_LIST_TITLE`

The assistant basically:
1. Checks what's the value of `DEFAULT_PENDING_LIST_TITLE` env var, in our case it's *To send e-mail*
2. Looks for the column in the board
3. When it finds the correct column, reads all the cards and checks what have the Approved/Not approved label
4. Parses the e-mail from the card description
5. Sends the approval/disapproval e-mail (below) and finally...

<div style="text-align:center;">
    <img src="https://i.imgur.com/2b7nYBW.png">
</div>

7. ...moves the card to `DEFAULT_DONE_LIST_TITLE` env var column, in our case it's *Done*

## Running
1. Clone the project and set up a virtual environment
2. Install dependencies with `pip install -r requirements.txt`
3. Create a `.env` file with the following required variables:
```bash
# SendGrid settings
SENDGRID_USERNAME='sendgrid_username'
SENDGRID_PASSWORD='sendgrid_password'

# Trello settings
TRELLO_KEY='key'
TRELLO_TOKEN='token'
DEFAULT_BOARD_ID='board_id'
DEFAULT_PENDING_LIST_TITLE='To send e-mail'
DEFAULT_DONE_LIST_TITLE='Done'
```
4. Run with `python manage.py runserver`

## Creating the IFTTT applet
1. Go to [New Applet](https://ifttt.com/create)
2. As the **trigger (this)**, select *Button widget* or anything you want
3. As the **action (that)**, select Webhooks
4. Run ngrok (remember to point it to the Django server port, which is `8000` by default) and copy its url
5. Set the ngrok URL provided to you as the Webhook URL
6. Click on **Create action**

## TODO
- [ ] Tests
- [ ] Disapproved flow