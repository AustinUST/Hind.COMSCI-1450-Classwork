

def play_bounded_guessing_game():
    import random as r
    secret_number = r.randint(1, 10)
    for att in range(3):
        guess = int(input("Enter your guess 1 to 10: "))
        if guess == secret_number:
            print("Congratulations! You Win!")
            return
        else:
            if att < 2:
                print("Wrong guess! Try again.")
    print(f"Game Over! The secret number was {secret_number}.") 

print(play_bounded_guessing_game())