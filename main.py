import time
from src.dijkstra import *
from src.tarjan import TarjanSPathTree


def main():

    print("Shortest path program")
    print("1. Implementation of algorithm \n2. Quit")
    user_choice = int(input("Please select your choice: 1 or 2"))

    while user_choice != 2:

        if user_choice == 1:
            print("Update for use of heap and array")

            while True:

                structure_choice = input("Input type of data structure (array, heap) you want to use: ")

                if structure_choice.lower() == "array":
                    print("to be updated")
                    break

                elif structure_choice.lower() == "heap":
                    TarjanSPathTree()
                    break

                else:
                    print("Please choose 'array' or 'heap'.")
                    structure_choice = input("Input type of data structure (array, heap) you want to use: ")

        else:
            print("Please choose 1 or 2.")

        print("Shortest path program")
        print("1. Implementation of algorithm \n2. Quit")
        user_choice = int(input("Please select your choice: 1 or 2"))

    print("Thank you!")


if __name__ == "__main__":
    main()