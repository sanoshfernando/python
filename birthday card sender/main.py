import pandas
import datetime as dt
import random
import smtplib

letters = []
my_email = "demiantestapp@gmail.com"
password = "owsibieqsoeuguiq"

now = dt.datetime.now()
today_day = now.day
today_month = now.month
data = pandas.read_csv("birthdays.csv")
matched = data[(data['day'] == today_day) & (data['month'] == today_month)]



if len(matched)>0:

    with open("letter_templates/letter_1.txt") as file:
        letter1 = file.read()
        letters.append(letter1)
    with open("letter_templates/letter_2.txt") as file:
        letter2 = file.read()
        letters.append(letter2)
    with open("letter_templates/letter_3.txt") as file:
        letter3 = file.read()
        letters.append(letter3)

    for index, row in matched.iterrows():
        name = row['name']
        to_email = row['email']
        year = row['year']
        random_letter = random.choice(letters)
        final_letter = random_letter.replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email,password)
            connection.sendmail(to_addrs=to_email,from_addr=my_email,msg=f"Subject: Happy Birthday!\n\n{final_letter}")

