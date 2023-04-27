import requests
from datetime import timedelta, date
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API = 'YOUR_NEWS_API_KEY'
STOCK_API = 'YOUR_STOCK_API_KEY'

ACCOUNT_SID = 'YOUR_ACCOUNT_SID'
AUTH_CODE = 'YOUR_AUTH_CODE'


news_parameters = {
    'q': COMPANY_NAME,
    'from': "2022-12-24",
    'to': "2022-12-25",
    'sortBy': 'popularity',
    'apiKey': NEWS_API,
}

stock_parameters = {
    'function': "TIME_SERIES_DAILY_ADJUSTED",
    'symbol': STOCK,
    'outputsize': "compact",
    'datatype': "json",
    'apikey': STOCK_API,
}

yesterday = (date.today() - timedelta(1)) - timedelta(1)
day_before_yesterday = yesterday - timedelta(1)

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()

stock = response.json()['Time Series (Daily)']
stock_yesterday = float(stock["{}".format(yesterday)]['4. close'])
stock_day_before_yesterday = float(stock["{}".format(day_before_yesterday)]['4. close'])
stock_difference = stock_yesterday - stock_day_before_yesterday
diff_in_percent = (abs(stock_difference) / stock_yesterday) * 100

up_down = None
if stock_difference > 0:
    up_down = '📈'
else:
    up_down = '📉'

if diff_in_percent > 1:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]

formatted_news = [f"{STOCK}: {up_down}{diff_in_percent:.2}%\n"
                  f"Headline: {article['title']}. \n" \
                  f"Brief: {article['description']}" for article in news_data]
client = Client(ACCOUNT_SID, AUTH_CODE)

for story in formatted_news:
    message = client.messages.create(
        from_='whatsapp:YOUR_TWILLIO_ACC_NUMBER',
        body='{}'.format(story),
        to='whatsapp:YOUR_NUMBER'
    )
