from newsapi import NewsApiClient
import requests


newsapi = '8e084233b8354fd2b7dd6a63cab59848'
send_msg = False
# Parameters
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "WVRZGNUSZAQUA0N5"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

"""params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",  # last 100 days
    "apikey": API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=params)
data = response.json()
time_series = data["Time Series (Daily)"]
available_dates = set(time_series.keys())  # all available trading dates as strings

def get_last_n_trading_days(n, available_dates):
    available_dates_sorted = sorted(available_dates, reverse=True)  # newest first
    return available_dates_sorted[:n]

# Get the last two trading days (e.g. yesterday and day before yesterday)
last_two_days = get_last_n_trading_days(2, available_dates)

# Get data for those dates
close_price = []
for date in last_two_days:
    day_data = time_series[date]
    print(f"{STOCK} on {date}:")
    close_price.append(float(day_data['4. close']))

price_dif = abs(close_price[0]-close_price[1])
print(round(price_dif,3))

yesterday_five_percentage = close_price[0]%5
print(yesterday_five_percentage)
if yesterday_five_percentage > price_dif:
    send_msg = True"""

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
url = (
    f"https://newsapi.org/v2/everything?"
    f"q=Tesla&"
    f"sortBy=popularity&"
    f"language=en&"
    f"pageSize=3&"
    f"apiKey={newsapi}"
)

response = requests.get(url)
data = response.json()

if data["status"] == "ok" and data["totalResults"] > 0:
    for article in data["articles"]:
        title = article.get('title', 'No Title')
        description = article.get('description', 'No Description')
        print(f"TSLA :\nPublished At: {article['publishedAt']}\nHeadline: {title}\nBrief: {description}\n")
else:
    print("No articles found or API error:")
    print(data)

#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

