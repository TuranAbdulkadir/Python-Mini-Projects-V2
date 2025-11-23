import tkinter as tk, random
def roll(): lbl.config(text=random.choice(['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']))
root = tk.Tk()
lbl = tk.Label(root, text="🎲", font=("Times", 100))
lbl.pack()
tk.Button(root, text="ROLL", command=roll).pack()
root.mainloop()