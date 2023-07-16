import smtplib
from config import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from routers.admin.v1.schemas import MailDetail
from fastapi import HTTPException, status

def send_mail_smtp(mail: MailDetail):
    password = config["email_password"]
    host = config["host"]
    port = config["port"]
    subject = mail.subject
    from_email = config["from_mail"]

    message = MIMEMultipart("alternative")
    message['Subject'] = subject
    message['From'] = f"{mail.title} <{from_email}>"
    message["To"] = mail.to_email
    template = f"""{mail.template}"""
    try:
        html_part = MIMEText(template, 'html')
        message.attach(html_part)
        smtp = smtplib.SMTP(host, port)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(from_email, password)
        smtp.sendmail(from_email, mail.to_email, message.as_string())
        smtp.quit()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="email not sent")
    return


def send_mail_smtp_two(title: str, to_email: str, subject: str, template: str):
    password = config["email_password"]
    host = config["host"]
    port = config["port"]
    from_email = config["from_mail"]

    message = MIMEMultipart("alternative")
    message['Subject'] = subject
    message['From'] = f"{title} <{from_email}>"
    message["To"] = to_email
    template = f"""{template}"""
    try:
        html_part = MIMEText(template, 'html')
        message.attach(html_part)
        smtp = smtplib.SMTP(host, port)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(from_email, password)
        smtp.sendmail(from_email, to_email, message.as_string())
        smtp.quit()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="email not sent")
    return