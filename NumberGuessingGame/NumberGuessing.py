import random
import tkinter as tk
from tkinter.ttk import Label
from tkinter import ttk
import pygame

root =tk.Tk()
root.geometry('600x500')
root.title("Number Guessing Game!")
root.resizable(True,True)
root.config(bg="lightblue")

label= tk.Label(root, font=('Verdana',15), bg='lightgrey', text='Number Guessing Game!')
label.pack(pady=20) #eh ta adiciona espaco di riba ku baxu

hint = tk.Label(root, font=('Verdana', 15), bg='lightgrey', text='Guess a number between 1-100!')
hint.pack(pady=20)

input_box= tk.Entry(root,bg='white', font=('Verdana',13), justify="center")
input_box.pack(pady=10)

att_box = tk.Label(root, font=('Verdana', 13), text="Attempts: 0/8")
att_box.pack(pady=10)

pygame.mixer.init()

def play_sound(filename):
    pygame.mixer.music.load(f"sounds/{filename}")
    pygame.mixer.music.play()


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
        hint.config(text="Too High", fg='red')
        play_sound("wrong.mp3")
 elif user_num < num:
       hint.config(text="Too Low", fg='red')
       play_sound("wrong.mp3")
 else:
     hint.config(text="You Won! :D", fg='green')
     root.config(bg='lightgreen')
     play_sound("Win.mp3")
     return
 attempts+=1
 att_box.config(text=f"Attempts: {attempts} /8")

 if attempts >= 8:
    #hint.config(text=("Too many failed attempts, You Lost!"))
    hint.config(text=((f'You Lost! :(\n The number was: {num}')))
    play_sound("Lose.mp3")
    return

def resetGame():
    global num, attempts, user_num
    num = random.randint(1,100)
    attempts= 0
    user_num=None
    hint.config(text='Guess a number between 1-100!') 
    input_box.delete(0, tk.END) #pa limpa kel input box (zero eh starting index ti fim di content of the entry widget)


guess_button= tk.Button(root, font=('Verdana',15), text="Guess",bg='lightgrey', command=game)
guess_button.pack(pady=10)

resetBut= tk.Button(text="Reset", font=('Verdana',12),bg='lightgrey', command=resetGame)
resetBut.pack(pady=10)

exit_button = tk.Button(root, font=('Verdana',12),bg='lightgrey', text='Exit',command=lambda: root.quit())
exit_button.pack(pady=10)


root.mainloop()