from tkinter import *
from tkinter import ttk

window = Tk()
window.configure(bg="#fff")
window.geometry("1920x1080")
window.title("VAKO tech Facial recognition system")

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Scan face to login")



img = PhotoImage(file='images/loginn.png')
Label(tab1, image=img, bg="white").place(x=200,y=200)

frame = Frame(tab1, width=500, height=500, bg="white")
frame1 = Frame(tab1, width=500, height=500, bg="white")
frame1.place(x=800,y=200)
heading = Label(frame1, text='Sign in', fg='red', bg='white', font=("Consolas", 25))
heading.pack()

lab4 = Label(frame1)
lab4.pack()

lab = Label(frame1, text='Admin no', fg='#57a1f8', bg='white', font=("Consolas", 15))
lab.pack()
user = Entry(frame1, font=("Arial",10, "bold"), bd=0, fg="black", width=35, bg="firebrick1")
user.pack()

lab4 = Label(frame1)
lab4.pack()

lab2 = Label(frame1, text='Name on Student Id', fg='#57a1f8', bg='white', font=("Consolas", 15))
lab2.pack()
user2 = Entry(frame1, font=("Arial",10, "bold"), bd=0, fg="black", width=35, bg="firebrick1")
user2.pack()

lab4 = Label(frame1)
lab4.pack()



lab4 = Label(frame1)
lab4.pack()

button = Button(frame1, text="Scan face to login",
                font=("Arial",10, "bold"),
                fg="black",
                width=30,

                )
button.pack()
notebook.add(tab2, text="Scan face for attendance")
notebook.pack(expand=True,fill="both")

Button(tab1, text="Press to scan your face",font=("Consolas", 25), width=50).pack(side=LEFT)
Label(tab2, text="Goodbye, this is tab 2")

window.mainloop()