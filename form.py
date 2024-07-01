import tkinter
root = tkinter.Tk()
root.title("Student registration form")

name_Label = tkinter.Label(root,text = "Enter name")
name_Label.pack()
name_textbox = tkinter.Entry(root)
name_textbox.pack()

email_Label = tkinter.Label(root,text = "Enter Email")
email_Label.pack()
email_textbox = tkinter.Entry(root)
email_textbox.pack()

phone_Label = tkinter.Label(root,text = "Enter Phone")
phone_Label.pack()
phone_textbox = tkinter.Entry(root)
phone_textbox.pack()

submit_button = tkinter.Button(root,text = "Submit")
submit_button.pack()
root.mainloop()


