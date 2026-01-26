
import smtplib
from email.message import EmailMessage
from typing import Optional

try:
    from twilio.rest import Client as TwilioClient
except Exception:
    TwilioClient = None  # Twilio is optional

class ConsoleNotifier:
    def send(self, subject: str, body: str):
        print(f"\n=== {subject} ===\n{body}\n")

class EmailNotifier:
    def __init__(self, host: str, port: int, user: str, password: str, from_email: str, to_email: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.from_email = from_email
        self.to_email = to_email

    def send(self, subject: str, body: str):
        if not all([self.host, self.port, self.user, self.password, self.from_email, self.to_email]):
            raise ValueError("Email notifier is not fully configured.")
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = self.from_email
        msg["To"] = self.to_email
        msg.set_content(body)
        with smtplib.SMTP(self.host, self.port) as server:
            server.starttls()
            server.login(self.user, self.password)
            server.send_message(msg)

class TwilioNotifier:
    def __init__(self, sid: str, auth_token: str, from_number: str, to_number: str):
        if TwilioClient is None:
            raise ImportError("twilio is not installed. Install it with 'pip install twilio'")
        self.client = TwilioClient(sid, auth_token)
        self.from_number = from_number
        self.to_number = to_number

    def send(self, subject: str, body: str):
        self.client.messages.create(
            from_=self.from_number,
            to=self.to_number,
            body=f"{subject}\n{body}",
        )
