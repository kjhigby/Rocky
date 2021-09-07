from tkinter import *
import random
import time

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)
user_choice = []
user_score = 0
computer_score = 0

game_on = True


def user_rock():
    global user_choice
    global computer_score
    global user_score
    user_choice == 'rock'
    computer_choice = random.choice(choices)

    if computer_choice == 'rock':
        canvas.itemconfig(card_title, text=f"You chose rock\n and so did the computer.\n You tied. 🤷")

    elif computer_choice == 'scissors':
        canvas.itemconfig(card_title, text=f"You chose rock\n and computer chose scissors.\n You win. 🏆")
        user_score += 1
        your_label.config(text=f"Your score:  {user_score}")

        print(f"Your score: {user_score}")

    elif computer_choice == 'paper':
        canvas.itemconfig(card_title, text=f"You chose rock\n and computer chose paper.\n You lose. 😢")
        computer_score += 1
        computer_label.config(text=f"Computer score:  {computer_score}")
        print(f"Computer score: {computer_score}")


def user_paper():
    global user_choice
    global computer_score
    global user_score

    user_choice == 'paper'
    computer_choice = random.choice(choices)

    if computer_choice == 'rock':
        canvas.itemconfig(card_title, text="You chose paper\n and computer chose rock.\n You win. 🏆")
        user_score += 1
        your_label.config(text=f"Your score:  {user_score}")

    elif computer_choice == 'scissors':
        canvas.itemconfig(card_title, text="You chose paper\n and computer chose scissors.\n You lose. 😢")
        computer_score += 1
        computer_label.config(text=f"Computer score:  {computer_score}")
        print(f"Computer score: {computer_score}")
    elif computer_choice == 'paper':
        canvas.itemconfig(card_title, text="You chose paper\n and computer chose paper.\n You tied. 🤷")


def user_scissors():
    global user_choice
    global computer_score
    global user_score
    user_choice == 'scissors'
    computer_choice = random.choice(choices)

    if computer_choice == 'rock':
        canvas.itemconfig(card_title, text="You chose scissors\n and computer chose rock.\n You lose. 😢")
        computer_score += 1
        computer_label.config(text=f"Computer score:  {computer_score}")
        print(f"Computer score: {computer_score}")
    elif computer_choice == 'paper':
        canvas.itemconfig(card_title, text="You chose scissors\n and computer chose paper.\n You win. 🏆")
        user_score += 1
        your_label.config(text=f"Your score:  {user_score}")

        print(f"Your score: {user_score}")
    elif computer_choice == 'scissors':
        canvas.itemconfig(card_title, text="You chose scissors\n and computer chose scissors.\n You tied. 🤷")


window = Tk()
window.title("Rock, Paper, Scissors")
window.config(padx=9, pady=10, bg="yellow")

canvas = Canvas(width=400, height=100)
card_front_image = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(50, 25, image=card_front_image)
card_title = canvas.create_text(200, 44, text="Choose rock, paper, or scissors\nto play against the computer.",
                                fill="#BF1363", font=("Ariel", 13, "bold"))
canvas.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

rock_img = PhotoImage(file="images/rock.png")
rock_button = Button(image=rock_img, command=user_rock)
rock_button.grid(row=3, column=0)

paper_img = PhotoImage(file="images/paper.png")
paper_button = Button(image=paper_img, command=user_paper)
paper_button.grid(row=3, column=1, pady=10, padx=10)

scissors_img = PhotoImage(file="images/scissors.png")
scissors_button = Button(image=scissors_img, command=user_scissors)
scissors_button.grid(row=3, column=2)

# question_label = Label(text="Click on rock, paper, or scissors to play against the computer.", font=("Ariel", 13, "bold"), fg=#BF1363"))
# question_label.grid(row=2, column=0, columnspan=3)

your_label = Label(text=f"Your score: {user_score}", font=("Courier", 14, "bold"), fg="white", bg="#FF616D")
your_label.grid(row=0, column=0)

computer_label = Label(text=f"Computer score:  {computer_score}", font=("Courier", 14, "bold"), fg="white",
                       bg="#04009A")
computer_label.grid(row=0, column=2)

window.mainloop()
