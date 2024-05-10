from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
from json.decoder import JSONDecodeError
#screen
screen=Tk()
screen.title("PASSWORD MANAGER")
screen.config(padx=50,pady=50)

#functions
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    letter_count=random.randint(6,8)
    numbers_count=random.randint(2,4)
    symbols_count=random.randint(1,3)
    l=[random.choice(letters) for letter in range(letter_count)]
    n=[random.choice(numbers) for letter in range(numbers_count)]
    s=[random.choice(symbols) for letter in range(symbols_count)]
    gen_pass=l+n+s
    random.shuffle(gen_pass)
    new_pass=""
    for i in gen_pass:
        new_pass+=i
    password_input.insert(0,new_pass)
    pyperclip.copy(new_pass)
    
def add_in_file():
    web=wesbite_input.get()
    user=username_input.get()
    password= password_input.get()
    data_dict={web:{user:password}}
    if len(user)==0 or len(password)==0:
        messagebox.showinfo(message="you can not enter empty password or username")
    else:
        msg=messagebox.askokcancel(message="Are you sure to save the changes?")
        if msg:
            try:
                file=open("tkinler\PASSWORD_MANAGER\DATA.json","r")
                try:
                    data=json.load(file)
                    data.update(data_dict)
                    file.close()
                except JSONDecodeError:
                    data={}
            except FileNotFoundError:
                with open("tkinler\PASSWORD_MANAGER\DATA.json","w") as file:
                    json.dump(data_dict,file,indent=4)    
            else:
                with open("tkinler\PASSWORD_MANAGER\DATA.json","w") as file:
                    json.dump(data,file,indent=4)
            
            wesbite_input.delete(0,END)
            password_input.delete(0,END)
            messagebox.askokcancel(message="successful")
def search():
    web=wesbite_input.get()
    found=False
    try:
        file=open("tkinler\PASSWORD_MANAGER\DATA.json","r")
        data_dict=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message="you do not have a password saved")    
    else:
        for (key,value) in data_dict.items():
            if web in key:
                messagebox.showinfo(message="you already have details saved about the website") 
                found=True
                break
        if not found:
            messagebox.showinfo(message="password does not exist")
    
    finally:
        file.close()            
            

#canvas
canvas=Canvas(width=200,height=200,)
imager=PhotoImage(file="tkinler\PASSWORD_MANAGER\logo.png")
canvas.create_image(100,100,image=imager)
canvas.grid(column=1,row=0)

#label
website_label=Label(text="website",font=("Arial",16,"bold"))
website_label.grid(column=0,row=1)

username_label=Label(text="username/E-mail",font=("Arial",16,"bold"))
username_label.grid(column=0,row=2)

password_label=Label(text="password",font=("Arial",16,"bold"))
password_label.grid(column=0,row=3)

#inputs
wesbite_input=Entry(width=35)
wesbite_input.grid(column=1,row=1,sticky="w")
wesbite_input.focus_set()

username_input=Entry(width=35)
username_input.grid(column=1,row=2,sticky="w")
username_input.insert(0,"ramneekjolly33@gmail.com")
password_input=Entry(width=21)
password_input.grid(column=1,row=3,sticky="w")

#buttons
password_button=Button(text="Generate Password",command=generate_password)
password_button.grid(column=2,row=3)

add_button=Button(text="Add",width=36,command=add_in_file)
add_button.grid(column=1,row=4,columnspan=2)

search_button= Button(text="Search",command=search)
search_button.grid(column=2,row=1)
screen.mainloop()