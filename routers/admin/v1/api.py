from fastapi import  APIRouter, Path, Query
from routers.admin.v1 import  schemas
from routers.admin.v1.crud import mails


router = APIRouter()


@router.post(
    "/send-mail",
    tags=["E-mail"]
)
def send_mail(
    mail: schemas.MailDetail
):
    data = mails.send_mail_smtp(mail=mail)
    return data


@router.post(
    "/send-mail-two",
    tags=["E-mail"]
)
def send_mail_two(
    title: str = Query(..., min_length=2, max_length=60),
    to_email: str = Query(..., min_length=5, max_length=50),
    subject: str = Query(..., min_length=2, max_length=70),
    template: str = Query(...)
):
    data = mails.send_mail_smtp_two(title=title, to_email=to_email, subject=subject, template=template)
    return data