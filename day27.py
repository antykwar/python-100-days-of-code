from tkinter import *


def main_button_clicked():
    user_input = float(miles_field.get())
    result = user_input * 1.609
    result_label['text'] = str(round(result, 3))


main_window = Tk()

main_window.title('Mile to Km Converter')
main_window.minsize(width=200, height=100)
main_window.iconphoto(False, PhotoImage(file='./day27_files/icon.png'))
main_window.config(padx=20, pady=20)

miles_field = Entry(font=('Arial', 24), width=5)
miles_field.grid(column=1, row=0, pady=10)
Label(text='Miles', font=('Arial', 24)).grid(column=2, row=0)

Label(text='is equal to', font=('Arial', 24)).grid(column=0, row=1, pady=10)
result_label = Label(text='0', font=('Arial', 24))
result_label.grid(column=1, row=1)
Label(text='Km', font=('Arial', 24)).grid(column=2, row=1)

main_button = Button(text='Calculate', font=('Arial', 24), command=main_button_clicked)
main_button.grid(column=1, row=2, pady=10)

main_window.mainloop()
