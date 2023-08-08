import tkinter
from tkinter import END

window = tkinter.Tk()
window.minsize(width=150, height=60)
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)
miles_entry = tkinter.Entry(width=10)
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)
my_label = tkinter.Label(text="is equal to")
my_label.grid(column=0, row=1)
my_miles = tkinter.Label(text="Miles")
my_miles.grid(column=2, row=0)
my_km = tkinter.Label(text="0")
my_km.grid(column=1, row=1)
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)
def calculate_km():
    miles_input = float(miles_entry.get())
    km_calculate = round((miles_input * 1.609),2)
    km_calculate = str(km_calculate)
    my_km.config(text=km_calculate)

calculate_button = tkinter.Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)
window.mainloop()
