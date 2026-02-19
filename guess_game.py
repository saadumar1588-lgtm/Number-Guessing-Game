n = 18
number_of_guesses = 6

while number_of_guesses > 0:
    guess_number = int(input("Enter your Number: "))
    
    if guess_number == n:
        print("Congrats You won the game")
        break
    
    elif abs(guess_number - n) <= 2:
        print("You are too close")
    
    elif guess_number < n:
        print("Number is too low")
    
    else:
        print("Number is too high")
        

    number_of_guesses -= 1
    print("You have", number_of_guesses, "attempts left")

if number_of_guesses == 0:
    print("Sorry you lose the game")
