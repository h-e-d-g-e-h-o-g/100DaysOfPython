import smtplib
import datetime as dt, random
with open("quotes.txt", "r") as f:
    list_of_quotes = f.readlines()

now = dt.datetime.now()
day_of_week = now.weekday()

my_email = "raholverma20@gmail.com"
my_password = "fttwxryohmtkqraa"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    if day_of_week == 1:
        connection.sendmail(from_addr=my_email, to_addrs="rahulver345@yahoo.com", msg=f"Subject:Tuesday motivation\n\n{random.choice(list_of_quotes)}")
