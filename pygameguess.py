import random
x=random.randint(1, 100)
for i in range(8):
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100. You have 7 tries."))
            break
        except ValueError:
            print("Please enter a valid integer.")
            continue
    if guess == x:
        print("Congratulations! You guessed the number.")
        break
    elif guess < x:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
else:
    print("Sorry, you didn't guess the number. The number was", x) 