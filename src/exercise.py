from random import randint


def main():
    # write your code below this line
    number = randint(1, 10)
    print("Computer guessed " + str(number))
    while True:

       
        user_input = input("higher, lower or correct: ")

        if user_input == "correct":
            print("Computer guessed correctly:")
            break
        elif user_input == "higher":
            new_guess = randint(number, 10)
            print("Computer guessed: " + str(new_guess))
        elif user_input == "lower":
            new_guess = randint(1, number)
            print("Computer guessed: " + str(new_guess))



if __name__ == '__main__':
    main()
