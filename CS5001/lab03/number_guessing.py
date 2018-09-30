import random as rnd 

def main():
    num = rnd.randint(1,50)
    print("Welcome to the Guessing Game!\nI picked a number between 1 and 50. Try and guess!")
    guess = int(input())
    counter = 1
    print("You guessed",guess)
    while(guess != num):
        counter += 1
        if abs(num - guess) > 20:
            print("You guess is icy freezing miserably cold.")
            guess = int(input())
        elif abs(num - guess <= 20) and abs(num - guess) > 13:
            print("You guess is extremely cold.")
            guess = int(input())
        elif abs(num - guess) <= 13 and abs(num - guess) > 8:
            print("Your guess is very cold.")
            guess = int(input())
        elif abs(num - guess) <= 8 and abs(num - guess) > 5:
            print("Your guess is cold.")
            guess = int(input())
        elif abs(num - guess) <= 5 and abs(num - guess) > 3:
            print("Your guess is warm.")
            guess = int(input())
        elif abs(num - guess) <= 3 and abs(num - guess) > 2:
            print("Your guess is very warm.")
            guess = int(input())
        elif abs(num - guess) <= 2 and abs(num - guess) > 1:
            print("Your guess is extremely warm.")
            guess = int(input())
        elif abs(num - guess) <= 1:
            print("Your guess is scalding hot.")
            guess = int(input())

    tryString = "try"
    if(counter > 1):
        tryString = "tries"
    if counter == 1:
        message = "That was lucky!"
    elif counter >= 2 and counter <=4:
        message = "That was amazing!"
    elif counter >= 5 and counter <= 6:
        message = "That was okay."
    elif counter == 7:
        message = "Meh."
    elif counter >= 9 and counter <= 9:
        message = "this is not your game."
    elif counter >= 10:
        message = "You are the worst guesser I've ever seen."
    print("Congratulations. You figured it out in",counter,tryString)
    print(message)
    if input() != "":
        print("Game Over: You won!\nYou guessed that the secret number was",num,"in",counter,tryString)
main()