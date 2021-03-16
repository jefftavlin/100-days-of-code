import smtplib
import datetime as dt
import pandas as pd
import random

my_email = 'jerusalemz.spider@gmail.com'
password = 'Manuela17@'
to_email = "jerusalemz.spider@yahoo.com"
yahoo_app_password = 'qscbwgzcpvigqyri'

df = pd.read_csv('quotes.txt', delimiter = '\t')
now = dt.datetime.now()

def send_email(from_email, to_email, password, msg):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=msg)


if dt.datetime.now().weekday() == 0:
    text = f"Subject:Quote of the Day ({now.day}/{now.month}/{now.year})\n\n" \
           f"{df.iloc[random.randint(0,100)].values[0]}"
    send_email(my_email, to_email, password, text)
