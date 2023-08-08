import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key = "N26QVJ1OPLFBD62L"
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": api_key
}
response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
response.raise_for_status()
data = response.json()
i = 0
yesterday_price = []
dates = []
for (key, value) in data["Time Series (Daily)"].items():
    if i < 2:
        yesterday_price.append(float(data["Time Series (Daily)"][key]["4. close"]))
        dates.append(key)
        i = i + 1
percentage_difference = (100*(yesterday_price[0] - yesterday_price[1]))/yesterday_price[1]
percentage_difference = round(percentage_difference, 2)
emoji = "📢"
if percentage_difference > 0 or percentage_difference < -0:
    stock_data_parameters = {
        'apiKey': "61a31f408f4e41d18206574ecc5bc166",
        'from': dates[1],
        'to': dates[0],
        'language': 'en',
        'sortBy': 'relevancy',
        'q': COMPANY_NAME
    }
    stock_response = requests.get(url="https://newsapi.org/v2/everything", params=stock_data_parameters)
    data_stock = stock_response.json()
    articles_list = data_stock['articles'][:3]
    # Creating Client for sending the message
    account_sid = "AC3f9285ad579f7c084dd3691342de395f"
    auth_token = "39249f9f8ace934b13433b774c26d2e8"
    client = Client(account_sid, auth_token)
    formatted_article = [f"{STOCK} {emoji} {percentage_difference}%\nHeadline: {article['title']}Brief: {article['description']}" for article in articles_list]
    for article in formatted_article:
        message = client.messages \
            .create(
            body=article,
            from_='+12546154115',
            to='+918860317648'
        )


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# 61a31f408f4e41d18206574ecc5bc166
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
