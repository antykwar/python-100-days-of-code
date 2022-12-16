import smtplib
import random
import datetime as dt

my_smtp = 'my_smtp'
my_email = 'my_email'
my_password = 'my_password'

if dt.datetime.now().isoweekday() != 1:
    exit()

with open('day32_challenge_1_files/quotes.txt') as library:
    quotes = library.readlines()
    quote_of_monday = random.choice(quotes)

with smtplib.SMTP(my_smtp) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f'Subject:Quote of this Monday\n\n{quote_of_monday}'
    )
