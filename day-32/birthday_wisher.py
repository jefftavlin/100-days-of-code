##################### Extra Hard Starting Project ######################]
import smtplib
import datetime as dt
import pandas as pd
import random

# 1. Update the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
df = pd.read_csv('birthdays.csv')

# 2. Check if today matches a birthday in the birthdays.csv
if day in list(df['day']):
    birthday_person = df[df['day'] == day]
    if month in list(birthday_person['month']):
        name = birthday_person['name'].values[0]
        email = birthday_person['email'].values[0]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
birthday_letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
with open(random.choice(birthday_letters)) as f:
    letter = f.read().replace('[NAME]', name)

# 4. Send the letter generated in step 3 to that person's email address.
my_email = ''
password = ''


def send_email(from_email, to_email, password, msg):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:Your special day.\n\n{msg}")


send_email(my_email, email, password, letter)
