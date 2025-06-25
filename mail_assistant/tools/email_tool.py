import smtplib
from email.message import EmailMessage


class EmailTool:
    def __init__(self):
        self.smtp_server = "smtp.your-company.com"
        self.smtp_port = 587
        self.username = "your-username"
        self.password = "your-password"

    def send_email(self, email, assignee):
        msg = EmailMessage()
        msg.set_content(email["body"])
        msg["Subject"] = email["subject"]
        msg["From"] = self.username
        msg["To"] = assignee

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.send_message(msg)
