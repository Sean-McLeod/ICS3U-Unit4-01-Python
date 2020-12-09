#!/usr/bin/env python3

# Created by Sean McLeod
# Created on December 2020
# This program can add all the whole numbers up to that number


def main():
    # this function can tell the user the total added number

    loop_counter = 0
    sum = 0

    print("This program can add up from 0 to the number you type.")
    print("For example, 5: 1+2+3+4+5=15")
    print("\n", end="")

    # input
    positive_integer_string = input("Enter in a positive integer: ")
    print("\n", end="")

    # process & output
    try:
        positive_integer = int(positive_integer_string)

        if positive_integer > 0:
            while loop_counter <= positive_integer:
                sum = sum + loop_counter
                loop_counter = loop_counter + 1

            print("The sum of numbers from 0 to {0} is {1}"
                  .format(positive_integer_string, sum))
        else:
            print("This is a negative integer")

    except Exception:
        print("This is not an integer")


if __name__ == "__main__":
    main()
