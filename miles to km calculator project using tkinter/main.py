from tkinter import *

window = Tk()
window.title("miles to kilometre calculator")
window.wm_minsize(width=500, height=300)
# window.config(padx=20,pady=20)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)
# miles_label.config(padx=20,pady=20)

kilometer_label = Label(text="kilometres")
kilometer_label.grid(column=2, row=1)
# kilometer_label.config(padx=20,pady=20)

is_equal_to_label = kilometer_label = Label(text="Is equal to")
is_equal_to_label.grid(column=0, row=1)
# is_equal_to_label.config(padx=20,pady=20)

miles = Entry(width=10)
miles.grid(column=1, row=0)


def convert_to_km():
    value = float(miles.get())
    converter = float(1.6)
    kilometres = value * converter
    converted_to_km.config(text=kilometres)


converted_to_km = Label(text=f"0")
# converted_to_km.config(padx=20,pady=20)
converted_to_km.grid(column=1, row=1)


button = Button(text="calculate", command=convert_to_km)
button.grid(column=1, row=2)
window.mainloop()
