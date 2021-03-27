##################### Extra Hard Starting Project ######################


import smtplib
import datetime as dt
import random
import pandas as pd
import os


letters = []

for dirname,_,files in os.walk("letter_templates"):
    for file in files:
        letters.append(os.path.join(dirname,file))


def make_letter(name):
    letterfile = random.choice(letters)
    with open(letterfile) as letterraw:
        letter = letterraw.read()

    letter = letter.replace("[NAME]",name)
    return letter

def send_mail(letter,address):
    # Your email account username and password eg my_email = test@email.com password = 123
    my_email = ""
    password = ""
    # Your stmp service provider eg. "smtp.gmail.com" for gmail
    with smtplib.SMTP("",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(to_addrs=address,from_addr=my_email,msg=f"Subject: Happy Birthday!!!\n\n{letter}")


bdays = pd.read_csv("birthdays.csv")
bdays = bdays.to_dict(orient="records")
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
date = now.day
for item in bdays:
    if (item["month"]==month and item["day"]==date):
        letter = make_letter(item["name"])
        send_mail(letter,item["email"])









