from enum import Enum
from pydantic import BaseModel, Field, ConfigDict, EmailStr


class SMTPServerSchema(str, Enum):
    yandex = "smtp.yandex.ru"
    gmail = "smtp.gmail.com"
    mail = "smtp.mail.ru"

class EmailSchema(BaseModel):
    to_email: EmailStr = Field(
        ...,
        description="Recipient's mailing address",
        examples=["your_email@domain.com"],
    )

    from_email: EmailStr = Field(
        ...,
        frozen=True,
        description="Sender's mailing address",
        examples=["your_email@domain.com"],
    )

    password: str = Field(
        ...,
        frozen=True,
        description="The password for the sender's mailbox",
        examples=["your_password"],
    )

    body: str = Field(
        "",
        description="Message text",
    )

    smtp_server: SMTPServerSchema = Field(
        "smtp.mail.ru",
        description="The address of the smtp server used",
        examples=["smtp.yandex.ru", "smtp.gmail.com", "smtp.mail.ru"],
    )

    port: int = Field(
        587,
        frozen=True,
        description="The number of the port used",
        examples=[8080, 5000],
    )

    subject: str = Field(
        "Сообщение",
        description="Topic of the letter"
    )

    model_config = ConfigDict(from_attributes=True)
