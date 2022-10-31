import random
import string
import pyperclip
import json

from tkinter import *
from tkinter import messagebox


class PasswordGenerator(Tk):
    def __init__(self):
        super().__init__()
        self._setup()
        self._prepare_screen()
        self._prepare_ui()
        self._database_name = 'day29_30_files/output/passwords.json'

    def start(self):
        self.mainloop()

    def _setup(self):
        self.title('Password Generator')
        self.iconphoto(False, PhotoImage(file='day29_30_files/lock.png'))
        self.resizable(False, False)

    def _prepare_screen(self):
        self.config(padx=30, pady=30)
        self._canvas = Canvas(
            width=200,
            height=200,
            border=0,
            highlightthickness=0
        )
        self._background_image = PhotoImage(file='day29_30_files/lock.png')
        self._canvas.create_image(100, 100, image=self._background_image)
        self._canvas.grid(column=1, row=0)

    def _prepare_ui(self):
        labels = {1: 'Website', 2: 'Email/Username', 3: 'Password'}
        for row, label in labels.items():
            form_label = Label(
                text=label + ':',
                font=('Courier', 18)
            )
            form_label.grid(column=0, row=row)
        self._site_field = Entry(font=('Courier', 18), width=24)
        self._site_field.grid(column=1, row=1)
        search_button = Button(text='Search', font=('Courier', 18), command=self._search_password)
        search_button.grid(column=2, row=1)
        self._site_field.focus()
        self._name_field = Entry(font=('Courier', 18), width=35)
        self._name_field.grid(column=1, row=2, columnspan=2)
        self._name_field.insert(END, 'some-email@test.com')
        self._password_field = Entry(font=('Courier', 18), width=24)
        self._password_field.grid(column=1, row=3)
        generate_button = Button(text='Generate', font=('Courier', 18), command=self._generate_password)
        generate_button.grid(column=2, row=3)
        add_button = Button(text='Add', font=('Courier', 18), width=36, command=self._add_password)
        add_button.grid(column=1, row=4, columnspan=2)

    def _add_password(self):
        site = self._site_field.get()
        email = self._name_field.get()
        password = self._password_field.get()

        new_data = {
            site: {
                'email': email,
                'password': password,
            }
        }

        if not site or not email or not password:
            messagebox.showwarning(title='Oops', message='All fields should be filled!')
            return

        try:
            with open(self._database_name, 'r') as passwords_list:
                current_data = json.load(passwords_list)
        except FileNotFoundError:
            with open(self._database_name, 'w') as passwords_list:
                json.dump(new_data, passwords_list, indent=4)
        else:
            current_data.update(new_data)
            with open('day29_30_files/output/passwords.json', 'w') as passwords_list:
                json.dump(current_data, passwords_list, indent=4)
        finally:
            self._site_field.delete(0, END)
            self._password_field.delete(0, END)

    def _generate_password(self):
        password_elements = random.choices(list(string.ascii_letters), k=random.randint(10, 16)) \
                            + random.choices(list(string.digits), k=random.randint(2, 6)) \
                            + random.choices(list(string.punctuation), k=random.randint(1, 4))
        random.shuffle(password_elements)
        self._password_field.delete(0, END)
        self._password_field.insert(END, ''.join(password_elements))
        pyperclip.copy(self._password_field.get())

    def _search_password(self):
        try:
            with open(self._database_name, 'r') as passwords_list:
                current_data = json.load(passwords_list)
        except FileNotFoundError:
            messagebox.showinfo(title='Oops', message='There is no data in database yet!')
        else:
            site = self._site_field.get()
            if site not in current_data.keys():
                messagebox.showinfo(title='Oops', message='There is no password for this site!')
                return
            data = current_data[site]
            messagebox.showinfo(title='Success', message=f"Name: {data['email']}\nPassword: {data['password']}")
        finally:
            return
