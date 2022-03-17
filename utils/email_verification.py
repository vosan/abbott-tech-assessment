import imaplib
import email
import os
import re
import pytz
from email.header import decode_header
from datetime import datetime

# account credentials
from constants import Constants
from properties import Properties

username = "codechallengeadc@outlook.com"
password = "P@ssword$1234"

# create an IMAP4 class with SSL
imap = imaplib.IMAP4_SSL("imap-mail.outlook.com")
# number of top emails to fetch
N = 3


def get_confirmation_code_from_email(timeout=Constants.MEDIUM_TIMEOUT) -> str:
    time_started = datetime.now()
    # authenticate
    imap.login(username, password)

    while (datetime.now() - time_started).seconds < timeout:
        status, messages = imap.select("INBOX")

        # total number of emails
        messages = int(messages[0])

        # cycle through the N most recent emails starting from the most recent one
        for i in range(messages, messages - N, -1):
            res, msg = imap.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    # parse a bytes email into a message object
                    msg = email.message_from_bytes(response[1])

                    # decode the email received date
                    email_received_time, encoding = decode_header(msg["Date"])[0]
                    if isinstance(email_received_time, bytes):
                        # if it's a bytes, decode to str
                        email_received_time = email_received_time.decode(encoding)
                    email_received_time = datetime.strptime(email_received_time, "%a, %d %b %Y %H:%M:%S %z")

                    # unify the datetime format
                    ver_code_request_time = datetime.fromisoformat(
                        os.environ[Properties.VERIF_CODE_REQUEST_TIME]).replace(tzinfo=pytz.UTC)
                    # if the email has been received before the test case started
                    if email_received_time < ver_code_request_time:
                        break

                    # decode email sender
                    sender, encoding = decode_header(msg.get("From"))[0]
                    if isinstance(sender, bytes):
                        # if it's a bytes, decode to str
                        sender = sender.decode(encoding)

                    # decode the email subject
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        # if it's a bytes, decode to str
                        subject = subject.decode(encoding)

                    if "@libreview.io" in sender and "verification code" in subject.lower():
                        # extract security code from message
                        code_msg = re.search(r'security code is: \d+', str(msg).lower()).group(0)
                        return "".join(filter(str.isdigit, code_msg))
                    else:
                        continue
    else:
        err = Exception("Could not get the verification code from email within the specified timeframe.")
    # close the connection and logout
    imap.close()
    imap.logout()

    if err:
        raise err
