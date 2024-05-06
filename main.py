import datetime as dt
import random
import smtplib
import pandas as pd

# Personal details removed for privacy.
MY_EMAIL = ""
PASSWORD = ""

# Returns a now object with attributes.
now = dt.datetime.now()
day = now.day
month = now.month
year = now.year

# Update birthdays.csv
# Read csv file into pandas DataFrame.
df = pd.read_csv("birthdays.csv", delimiter=",")

# Iterate rows to return a list of tuples.
result = [row for row in zip(df['name'], df['email'], df['year'], df['month'], df['day'])]
# print(result)

birthdays_today = []
for x in result:
    # Check if today matches a birthday in the birthdays.csv
    if x[3] == month and x[4] == day:
        birthdays_today.append(x)
for x in birthdays_today:
    # If today is his/her birthday, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    TEMPLATE_NUMBER = "letter_" + (str(random.randint(1, 3)) + ".txt")
    # File directory removed for privacy.
    with open(
            '' + TEMPLATE_NUMBER,
            'r') as file:
        name = x[0]
        email = x[1]
        letter = file.readlines()
        content = ""
        for alphabet in letter:
            content = content + alphabet
        content = content.replace("[NAME]", x[0])
        content = content.replace("Angela", "Sufyan")
        print(content)
    # Send the letter generated above to the person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{content}".encode("utf-8"))
        print(f"\nThe birthday email has been sent to {name} at {email} using {TEMPLATE_NUMBER}.\n")
