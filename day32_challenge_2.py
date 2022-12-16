import smtplib
import random
import datetime as dt
import pandas as pd

my_smtp = 'my_smtp'
my_email = 'my_email'
my_password = 'my_password'

try:
    data_frame = pd.read_csv(f'day32_challenge_2_files/birthdays.csv')
except FileNotFoundError:
    raise FileNotFoundError(
        'Missing birthdays data! Please, rename birthdays.csv.example to birthdays.csv and fill it :)'
    )

current_date = dt.datetime.now()

birthdays = data_frame.loc[(data_frame['month'] == current_date.month) & (data_frame['day'] == current_date.day)]
if len(birthdays) == 0:
    print('No birthdays today :(')
    exit(0)
birthdays = birthdays.to_dict(orient='index')

with smtplib.SMTP(my_smtp) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)

    for _, birthday in birthdays.items():
        mail_template_number = random.randint(1, 3)
        mail_template = f'day32_challenge_2_files/letter_{mail_template_number}.txt'
        with open(mail_template) as mail:
            mail_text = mail.read()
        mail_text = mail_text.replace('[NAME]', birthday['name'])
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f'Subject:Happy birthday!\n\n{mail_text}'
        )
