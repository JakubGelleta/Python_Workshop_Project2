import random


def get_number():
    """
    Function to get number from user.
    Try until user give proper number.
    :return:
    """

    while True:
        try:
            result = int(input("Choose your number: "))
            break
        except ValueError:
            print("It's not a number...")
    return result


def get_numbers():
    """
    Program is getting 6 numbers from user using function get_number().
    :return:
    """

    result = []

    while len(result) < 5:
        number = get_number()

        if number not in range(1, 50):
            print("Value out of range... Choose correct number in range 1-49")

        elif number not in result:
            result.append(number)


    return result

def print_numbers(numbers):

    """
    print numbers in ascending order
    :param numbers: list of numbers
    """

    print(", ".join(str(number) for number in sorted(numbers)))

def computer_draw():

    """
    Computer is drawing 6 random numbers in rage 1-49
    :rtype: list
    :return:
    """

    numbers = list(range(1, 49))
    random.shuffle(numbers)
    return numbers[:6]

def lottery():

    """Main function of our game"""

    user_numbers = get_numbers()
    print("Your numbers: ")
    print_numbers(user_numbers)

    computer_numbers = computer_draw()
    print("Computer draw: ")
    print_numbers(computer_numbers)

    hits = 0

    for number in user_numbers:
        if number in computer_numbers:

            hits += 1

    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")


if __name__ == '__main__':
    lottery()
