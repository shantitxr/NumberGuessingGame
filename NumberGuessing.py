import random
import tkinter as tk
from tkinter.ttk import Label
from tkinter import ttk

root =tk.Tk()
root.geometry('600x500')
root.title("Number Guessing Game!")
root.resizable(True,True)
root.config(bg="lightblue")

label= tk.Label(root, font=('Verdana',15), bg='lightgrey', text='Number Guessing Game!')
label.pack(pady=20) #eh ta adiciona espaco di riba ku baxu

input_box= tk.Entry(root,bg='white', font=('Verdana',13), justify="center")
input_box.pack(pady=10)

hint = tk.Label(root, font=('Verdana', 15), bg='lightgrey', text='Guess a number between 1-100!')
hint.pack(pady=20)

att_box = tk.Label(root, font=('Verdana', 13), text="Attempts: 0")
att_box.pack(pady=10)

num = random.randint(1,100)
attempts= 0
user_num=None
def game():
 global attempts, user_num
 
 try:
      user_num= int(input_box.get())
      if user_num < 1 or user_num > 100:
          #hint.config(text=("Please input a number between 1-100"))
          raise ValueError
 except ValueError:
     hint.config(text=("Please type a valid number (from 1-100)"))
     return


 if user_num > num:
        hint.config(text=("Too High"))
 elif user_num < num:
       hint.config(text=("Too Low"))
 else:
     hint.config(text=("You Won!"))
     return
 attempts+=1
 att_box.config(text=f"Attempts: {attempts}")

 if attempts >= 8:
    #hint.config(text=("Too many failed attempts, You Lost!"))
    hint.config(text=((f'Too many failed attempts, You Lost!\n The number was: {num}')))
    return

def reset():
    global num, attempts, user_num
    num = random.randint(1,100)
    attempts= 0
    user_num=None
    hint.config(text='Guess a number between 1-100!') 
    input_box.delete(0, tk.END) #pa limpa kel input box (zero eh starting index ti fim di content of the entry widget)


guess_button= tk.Button(root, font=('Verdana',15), text="Guess!",bg='lightgrey', command=game)
guess_button.pack(pady=10)

resetBut= tk.Button(text="Reset", font=('Verdana',12),bg='lightgrey', command=reset)
resetBut.pack(pady=10)

exit_button = tk.Button(root, font=('Verdana',12),bg='lightgrey', text='Exit',command=lambda: root.quit())
exit_button.pack(pady=10)

root.mainloop()