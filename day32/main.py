import datetime as dt
import pandas
import random
import smtplib
NAME = ""
PASSWORD = ""
today_tuple = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    for today_tuple in birthdays_dict:
        birthday_person = birthdays_dict[today_tuple]
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp-mail.outlook.com") as connection:
            connection.starttls()
            connection.login(NAME, PASSWORD)
            connection.sendmail(
                from_addr=NAME,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday\n\n{contents}"
            )

# Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
