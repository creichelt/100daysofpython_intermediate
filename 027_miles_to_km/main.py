from tkinter import *

def miles_to_km():
    miles = float(input_label.get())
    km = miles*1.60934
    result_label.config(text=f'{km}')

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

# Entry
input_label = Entry(width=7)
input_label.grid(column=1, row=0)

# labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
km_label = Label(text='Km')
km_label.grid(column=2, row=1)
result_label = Label(text='0')
result_label.grid(column=1, row=1)

# button
calc_button = Button(text='calculate', command=miles_to_km)
calc_button.grid(column=1, row=2)

mainloop()
