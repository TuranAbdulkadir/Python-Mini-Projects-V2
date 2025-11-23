import tkinter as tk
from time import strftime
def update_clock():
    lbl.config(text=strftime('%H:%M:%S'))
    lbl.after(1000, update_clock)
app = tk.Tk()
app.title("Clock")
app.configure(bg="black")
lbl = tk.Label(app, font=('Arial', 50, 'bold'), bg='black', fg='#00ff00')
lbl.pack(pady=20)
update_clock()
app.mainloop()