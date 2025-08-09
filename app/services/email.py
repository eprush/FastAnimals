import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.schemas.email import EmailSchema


class EmailService:
    def __init__(self, to_email, from_email, password: str) -> None:
        self._email_info: EmailSchema = EmailSchema(
            to_email=to_email,
            from_email=from_email,
            password=password,
        )

    def send_email(self, message: str) -> None:
        self._email_info.body = message
        try:
            # Создаем сообщение
            msg = MIMEMultipart()
            msg['From'] = self._email_info.from_email
            msg['To'] = self._email_info.to_email
            msg['Subject'] = self._email_info.subject

            # Добавляем текст сообщения
            msg.attach(MIMEText(self._email_info.body, 'plain'))

            # Подключаемся к SMTP серверу и отправляем письмо
            server = smtplib.SMTP(self._email_info.smtp_server, self._email_info.port)
            server.starttls()  # Защищенное соединение
            server.login(self._email_info.from_email, self._email_info.password)
            server.sendmail(self._email_info.from_email, self._email_info.to_email, msg.as_string())
            server.quit()

            print("Письмо успешно отправлено!")
        except Exception as e:
            print(f"Произошла ошибка при отправке письма: {str(e)}")
