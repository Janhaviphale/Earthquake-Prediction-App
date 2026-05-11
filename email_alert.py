import smtplib
from email.mime.text import MIMEText

def send_email_alert(message):

    sender_email = "janhaviphale06@gmail.com"

    sender_password = "obls xrur vrlz avew"

    receiver_email = "janhaviphale06@gmail.com"

    msg = MIMEText(message)

    msg['Subject'] = "Earthquake Alert"

    msg['From'] = sender_email

    msg['To'] = receiver_email

    server = smtplib.SMTP(
        'smtp.gmail.com',
        587
    )

    server.starttls()

    server.login(
        sender_email,
        sender_password
    )

    server.send_message(msg)

    server.quit()

    print("Email Alert Sent Successfully")