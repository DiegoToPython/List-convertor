# imports
import os
from tkinter import *

# Fonctions

def convert():
    try:
        value = text.get("1.0", "end-1c")
        with open(f'{value}') as f:
            lines = f.readlines()
            lines2 = [x.replace('\n', '') for x in lines]
            value.replace(".txt", "")
            with open(f"{value}_python_list.txt","x") as nf:
                file_list = []
                file_list.append(lines2)
                file_ctx = str(file_list)
                nf.write(file_ctx)

        root.destroy()
        Nroot = Tk()
        Nroot.title("List Convertor")
        Nroot.geometry("420x500")
        Nroot.minsize(420, 500)
        Nroot.maxsize(420, 500)
        Nroot.config(background="light green")

        main_title = Label(Nroot, text="Txt file succesfuly converted.",
                        font=("Calibri", 20), bg="green", fg="white")
        main_title.grid(padx=50, pady=200)

        def update_root():
            Nroot.destroy()

        Nroot.after(2000, update_root)

    except Exception as e:
        troot = Tk()
        troot.title("List Convertor")
        troot.geometry("420x500")
        troot.minsize(420, 500)
        troot.maxsize(420, 500)
        troot.config(background="red")

        main_title = Label(troot, text="Specify a valid file or path.",
                           font=("Calibri", 20), bg="dark red", fg="white")
        main_title.grid(padx=50, pady=200)

        def update():
            troot.destroy()

        troot.after(2000, update)




# Fenêtre

root = Tk()
root.title("List Convertor")
root.geometry("420x500")
root.minsize(420, 500)
root.maxsize(420, 500)
root.config(background="light grey")

main_title = Label(root, text="Convert you .txt files to python lists.",
                   font=("Calibri", 15),bg="light grey" ,fg="black")
main_title.grid(padx=50,pady=20)

text = Text(root)
text.insert(INSERT, "Enter your path.")
text.config(bg="white", fg="black", height=1, width=30, font=("Calibri", 15))
text.grid(padx=50, pady=150)


button = Button(root, text="Convert", font=("Calibri", 15), bg="grey",
                fg="black", activebackground="light grey", activeforeground="grey",
                width=15, command=convert)
button.grid(padx=50, pady=0)

root.mainloop()