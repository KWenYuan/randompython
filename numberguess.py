import random

print("Input 2 numbers and guess the random number the computer chose")

def guess_game():
    # Lets the user choose lower limit, higher limit and number of tries
    try:
        first_num = int(input("Input the lower limit number: "))
        second_num = int(input("Input the higher limit number: "))
        number_of_chance = int(input("Input the number of tries: "))
    except:
        print("Input only numbers!")
        guess_game()

    # Filter out input that doesn't make sense
    if first_num > second_num:
        print("Lower limit number must be lower than Higher limit number")
        guess_game()
    elif number_of_chance == 0:
        print("Number of chance must be more than 0")
        guess_game()
    else:
        print(f"The computer is going to randomly select a number between {first_num} and {second_num}")
        print(f"You have {number_of_chance} tries")
        global guess_num
        guess_num = random.randint(first_num, second_num)
        print(guess_num)
        for x in range(1, number_of_chance + 1, 1):
            user_guess = int(input(f"Guess {x} : "))
            if user_guess == guess_num:
                print(f"Congrats! The number is {guess_num}")
                break
            elif user_guess < guess_num:
                print("The number is higher")
            elif user_guess > guess_num:
                print("The number is lower")
        print("Game has ended")
        # Whether user wants to continue
        user_play = input("Type 'C' to continue or any other keys to quit: ").capitalize()
        if user_play == 'C':
            guess_game()
        else:
            quit()

# Start the game
guess_game()