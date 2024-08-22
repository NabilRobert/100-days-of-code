import requests
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "324bbb0988654c33895234d4ae7d7d61"
AA_API_KEY = "6QBLIG1ED72CW7FL"

MY_EMAIL = "robertfostersender@gmail.com"
MY_PASSWORD = "mbrjdcihtpyxwpqt"
TO_EMAIL = "nabilopenforbusiness@gmail.com"

AA_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": f"{STOCK_NAME}",
    "apikey": f"{AA_API_KEY}"
}
NEWS_PARAMS = {
    "apiKey": "324bbb0988654c33895234d4ae7d7d61",
    # "country" : "us",
    "qInTitle": f"{COMPANY_NAME}"
}
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

response = requests.get(STOCK_ENDPOINT, params=AA_PARAMS)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing = yesterday_data["4. close"]
print(yesterday_closing)
# TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing)
# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = abs(float(yesterday_closing) - float(day_before_yesterday_closing))
print(positive_difference)
# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference_perc = round(positive_difference / float(yesterday_closing)) * 100
up_down = None
if difference_perc > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
print(difference_perc)
# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(difference_perc) > 0:
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    news_articles = news_response.json()["articles"]
    three_articles = news_articles[:3]
    formatted_text = [f'Headline: {article['title']}. \nBrief: {article['description']}' for article in three_articles]
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=f"{MY_EMAIL}", password=f"{MY_PASSWORD}")
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=TO_EMAIL,
        msg=f"Subject:{STOCK_NAME}:{up_down}{positive_difference}% \n\n {formatted_text}"
    )
# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
