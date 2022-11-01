#!/usr/bin/env python3
# Created by: Katie G
# Created on: October 31st, 2022
# This program asks the user for a positive number,
# then uses a try catch statement and an if statement
# to make sure the user input is actually an integer,
# then the program uses a while loop to add the
# loop counter (which represents the numbers between 0
# and the user input) to the sum until the loop counter
# is greater than the user input, then the program displays
# the sum, thanks the user for using the program, and ends.


def main():
    # initializing sum and loop counter variables.
    sum = 0
    loop_counter = 0

    # introducing the function of the program to the user.
    print(
        "Hello! This program is gonna tell you the sum of "
        "all the numbers in between 0 and the one you enter :D "
    )

    # getting the user's input
    user_num = input("Please give me a positive number :) ")

    # initializing the user_num_as_int variable to prevent a value error
    # in the try...catch statement
    user_num_as_int = user_num

    # try...catch statement to check if the user's input is valid.
    try:
        user_num_as_int = int(user_num)
        if user_num_as_int >= 0:
            while loop_counter <= user_num_as_int:
                sum = sum + loop_counter
                loop_counter = loop_counter + 1
            print(
                "The sum of the numbers between 0 and "
                "{} is: {}".format(user_num_as_int, sum)
            )
        else:
            print(
                "Sorry, this is not a valid input. "
                "Please only input a positive integer."
            )
    except Exception:
        print("Sorry, this is not a valid input. Please only input a positive integer.")
    finally:
        print("Thank you for using this program!")


if __name__ == "__main__":
    main()
