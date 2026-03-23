import tkinter as tk
from tkinter import messagebox
import validators
import webbrowser

on_screen = False
fl = None

def check_inputs(email):
    validation = validators.email(email)

    if validation != True:
        messagebox.showerror("Error", "You did not enter a valid email address!")
        return False
    
    else:
        return True

def make_link():
    global on_screen, fl
    email = email_entry.get()
    subject = subject_entry.get()
    body = body_entry.get()
    base_url = "mailto:"

    email_check = check_inputs(email)

    if email_check != True:
        return

    final_link = f"{base_url}{email}?subject={subject}&body={body}"

    if on_screen == True:
        fl.destroy()

    fl = tk.Text(root, height=10, wrap=tk.WORD,
                 state="normal",
                 background=root.cget("bg"),
                 relief="flat",
                 highlightthickness=0,
                 borderwidth=0)
    fl.insert("1.0", final_link)
    fl.config(state=tk.DISABLED)
    fl.pack()
    on_screen = True

root = tk.Tk()
root.geometry("600x400")
root.maxsize(600, 400)
root.minsize(600, 400)
root.title("Mail To Link Maker")

email_label = tk.Label(root, text="Email Address")
email_label.pack()
email_entry = tk.Entry(root, width=20)
email_entry.pack(pady=(0, 10))

subject_label = tk.Label(root, text="Subject")
subject_label.pack()
subject_entry = tk.Entry(root, width=20)
subject_entry.pack(pady=(0, 10))

body_label = tk.Label(root, text="Body")
body_label.pack()
body_entry = tk.Entry(root, width=20)
body_entry.pack(pady=(0, 10))

create_button = tk.Button(root, text="Create Link", command=make_link)
create_button.pack(pady=10)


link_label = tk.Label(text="https://tylercaselli.com", fg="blue", cursor="hand2")
link_label.bind("<Button-1>", lambda e: webbrowser.open("https://tylercaselli.com"))
link_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()