import os
from twilio.rest import Client
import requests
import yfinance as yf
import pandas as pd
from datetime import date, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
tsla = yf.download(STOCK)['Adj Close']

yesterday = tsla.tail(2).head(1)
before_yesterday = tsla.tail(3).head(1)
before_yesterdays_date = str(before_yesterday.reset_index()['Date'].values[0]).split('T')[0]
yesterdays_date = str(yesterday.reset_index()['Date'].values[0]).split('T')[0]

percentage_change = round((yesterday.values[0] - before_yesterday.values[0]) / before_yesterday.values[0] * 100, 2)

news_key = os.environ['NEWS_API_KEY']
endpoint = 'https://newsapi.org/v2/everything'

params = {
    'qInTitle': COMPANY_NAME,
    'apikey': news_key,
    'sortBy': 'popularity',
    'from': before_yesterdays_date,
    'to': yesterdays_date,
}

response = requests.get(endpoint, params=params).json()['articles'][0:3]
titles = []
brief = []
urls = []

for r in response:
    titles.append(r['title'])
    brief.append(r['description'])
    urls.append(r['url'])

if percentage_change > 0:
    symbol = '🔺'
else:
    symbol = '🔻'

# Optional: Format the SMS message like this:
"""
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
messages = []

for i in range(3):
    message = f"{STOCK}:{symbol}{percentage_change}%\n" \
              f"Headline: {titles[i]}\n" \
              f"Brief: {brief[i]}\n" \
              f"URL: {urls[i]}"
    messages.append(message)

for i in range(3):
    message = client.messages \
        .create(
        body=messages[i],
        from_='+17812096036',
        to='+15147051028'
    )

print(message.sid)
