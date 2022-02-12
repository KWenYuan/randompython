import random
import sys

r = "rock"
p = "paper"
s = "scissors"
user_point = 0
computer_point = 0
draw = 0

print("Welcome to rock paper scissors")
print("First to 10 points wins!")

def draw_func():
    print("Its a DRAW")
    global draw
    draw += 1

def win_func():
    print("You won!")
    global user_point
    user_point += 1

def lose_func():
    print("You lost!")
    global computer_point
    computer_point += 1

while True:

    print(f"User : {user_point}, Computer : {computer_point}, Draw : {draw}")
    print("Choose 'R' for rock, 'P' for paper or 'S' for scissors or 'Q' to quit")
    user_input = input("").capitalize()

    if user_input == "R":
        user_choice = r
    elif user_input == "P":
        user_choice = p
    elif user_input == "S":
        user_choice = s
    elif user_input == "Q":
        print("Thank you for playing!")
        sys.exit()
    else:
        print("Choose between R, P or S only")
        continue

    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_choice = r
    elif computer_choice == 2:
        computer_choice = p
    else:
        computer_choice = s
    print(f"The computer chose... {computer_choice}")

    if user_choice == r and computer_choice == r:
        draw_func()
    elif user_choice == r and computer_choice == p:
        lose_func()
    elif user_choice == r and computer_choice == s:
        win_func()

    if user_choice == p and computer_choice == p:
        draw_func()
    elif user_choice == p and computer_choice == s:
        lose_func()
    elif user_choice == p and computer_choice == r:
        win_func()

    if user_choice == s and computer_choice == s:
        draw_func()
    elif user_choice == s and computer_choice == r:
        lose_func()
    elif user_choice == s and computer_choice == p:
        win_func()

    if user_point >= 10:
        print("You have won the game!")
        sys.exit()
    elif computer_point >= 10:
        print("You have lost the game!")
        sys.exit()

