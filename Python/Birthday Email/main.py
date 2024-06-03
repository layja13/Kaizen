import random
import smtplib
import datetime as dt
from quotes import list

my_email= "email@gmail.com"
password="tfhxejcmokuxqqvg"

now = dt.datetime.now()
weekday= now.weekday()

date_of_birth = dt.datetime(year =2024, month=9, day=20)
date_to_remember_and_see_and_achieve = dt.datetime(year=2024,month=9, day=30)
date_to_see = dt.datetime(year=2025,month=9, day=30)
date_three = dt.datetime(year=2024,month=9, day=29)


with smtplib.SMTP("smtp.gmail.com") as connection:
        if now.day == date_of_birth.day and now.month==date_of_birth.month and now.year==date_of_birth.year:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="ejemplo_email@gmail.com",
                                msg=f"Subject: message")

        elif now.day == date_Carolina_Te_Amo.day and now.month==date_three.month and now.year==date_three.year:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="ejemplo_email@gmail.com",
                                msg=f"Subject: Luis Morales Layja, del pasado, fecha 28/07/2023")


        elif now.day == date_to_see.day and now.month == date_to_see.month and now.year == date_to_see.year:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="ejemplo_email@gmail.com",
                                msg=f"mensaje d eun año atras")


        elif now == date_to_see:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="luislayja13@gmail.com",
                                msg=f"mensaje de dos años atras.")


        elif weekday == 0 or weekday == 4:
            c = random.choice(list)
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="email@gmail.com",
                                msg=f"Subject: Message of the day\n\n {c}")
