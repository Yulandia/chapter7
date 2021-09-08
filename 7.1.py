import random

def generateNumber():
    random_number = random.randint(0, 50)
    return random_number


def askNumber():
    user_number = int(input("Guess the number: "))
    return user_number


def check_user_number(user_number, random_number):
    if user_number > random_number:
        return "The value is too high"
    elif user_number < random_number:
        return "The value is too low"
    else:
        return "You guessed correctly"

def main():
    random_number = generateNumber()
    guessed_incorrectly = True
    number_of_guesses = 7

    while guessed_incorrectly and number_of_guesses > 0:
        number_of_guesses -= 1
        user_number = askNumber()
        message = check_user_number(user_number,random_number)

        if message == "You guessed correctly":
            guessed_incorrectly = False

        print(message)

    if number_of_guesses <=0:
        print("You reached the number of attempts")


main()