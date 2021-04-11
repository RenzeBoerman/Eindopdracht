import tkinter as tk


root = tk.Tk()
root.title("Hoofdmenu")
root.geometry('200x200')

label_text = tk.Label(
    text="Maak een keuze:"
)
label_text.grid(row=1, column=2)

def to_btw():
    print("btw pressed")
    exec(open('btw.py').read())


btn_btw = tk.Button(
    root,
    text="bereken btw",
    command= to_btw
)
btn_btw.grid(row=2, column=2)


def to_rekenmachine():
    print("rekenmachine pressed")
    exec(open('rekenmachine.py').read())

btn_rekenmachine = tk.Button(
    root,
    text="rekenmachine",
    command= to_rekenmachine
)

btn_rekenmachine.grid(row=3, column=2)

root.mainloop()