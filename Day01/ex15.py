import random
number = random.randint(1, 1000)
nb_lives = 10
guess = 0

while guess != number:
    if nb_lives == 0:
        print("Tu as perdu")
        break
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == number:
        print("You guessed right")
    if guess > number:
        print("Too high")
    if guess < number:
        print("Too low")
    nb_lives -= 1

