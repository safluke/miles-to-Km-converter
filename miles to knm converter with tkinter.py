"""
Miles to Km Converter using TKinter
"""

import tkinter as tk

def button_clicked():
    miles=float(miles_input.get())
    km=round(miles/5*8)
    kmoutput_label.config(text=f"{km}")
    


window = tk.Tk()
window.title("Miles to Km Converter")
window.minsize(width=150, height=100)
window.config(padx=60, pady=60)

#Label
isequal_label = tk.Label(text="is equal to", font=("Arial",16))
isequal_label.grid(column=0, row=1)

#Label
miles_label = tk.Label(text="miles", font=("Arial",16))
miles_label.grid(column=2, row=0)

#Label
km_label = tk.Label(text="Km", font=("Arial",16))
km_label.grid(column=2, row=1)

#label
kmoutput_label = tk.Label(text="0", font=("Arial",16))
kmoutput_label.grid(column=1, row=1)

#entry
miles_input = tk.Entry(width=10)
#print(input.get())
miles_input.grid(column=1, row=0)

#button
button=tk.Button(text="Convert",command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()