from tkinter import Tk, ttk, StringVar

root = Tk()

root.minsize(500,500)
root.title("Haushaltsbuch")
btn = ttk.Button(root, text="Beenden", command=root.quit)
btn.grid(row=1,column=1)
eingabe = "hallo"
textvar = StringVar()
textvar.set(eingabe)
entry = ttk.Entry(root, width=15, textvariable=textvar, font=("Arial",12,"bold"), state="readonly")
entry.grid(row=0, column=0)

root.mainloop()