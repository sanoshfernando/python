import smtplib
import random
import datetime as dt

email = "demiantestapp@gmail.com"
password = "owsibieqsoeuguiq"
now = dt.datetime.now()
day = now.weekday()
if day ==0:
    with open("quotes.txt","r") as data:
        quotes = data.readlines()
        r_quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email,password)
        connection.sendmail(from_addr=email,to_addrs=email,msg=f"Subject:Monday's Motivation\n\n{r_quote}")