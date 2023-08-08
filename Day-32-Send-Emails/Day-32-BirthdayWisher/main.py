##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

import datetime as dt
import pandas
# 4. Send the letter generated in step 3 to that person's email address.
import random
import smtplib

list_of_letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
random_letter = random.choice(list_of_letters)
now = dt.datetime.now()
date = now.day
month = now.month
print(now.date())
date_tuple = (date, month)
birthday_data = pandas.read_csv("birthdays.csv")
my_email = "raholverma20@gmail.com"
my_password = "fttwxryohmtkqraa"
birthday_dict = {(row['day'], row['month']): row for (index, row) in birthday_data.iterrows()}
# print(birthday_dict)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    if date_tuple in birthday_dict:
        birthday_name = birthday_dict[date_tuple]['name']
        birthday_email = birthday_dict[date_tuple]['email']
        with open(random_letter) as file:
            content = file.read()
            content = content.replace("[NAME]", birthday_name)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_email, msg=f"Subject:Letter to the dearest\n\n{content}")



