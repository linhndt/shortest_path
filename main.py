import time
from src.dijkstra import *
from src.tarjan import TarjanSPathTree, tarjanstpath
from src.ultilities import convert_to_adj_list
from src.centrality import FloretineMarriage
from src.graph_generator import graph_generator


def main():

    print("Shortest path program")
    print("1. Implementation of algorithms for large graph \n2. Solve Ballyskate problem \n"
          "3. Solve Padgett Marriage Alliances \n4. Quit")
    user_choice = int(input("Please select your choice: 1, 2 or 3 \n"))

    while user_choice != 4:

        if user_choice == 1:
            print("You need to create a graph first.")
            graph_generator()

            print("Based on time complexity, we use an array data structure for the dense graph,"
                  "and a min heap for the sparse graph.")

            while True:

                structure_choice = input("Input type of data structure (array, heap) you want to use: ")

                if structure_choice.lower() == "array":
                    DjikstraSthTree()
                    break

                elif structure_choice.lower() == "heap":
                    TarjanSPathTree()
                    break

                else:
                    print("Please choose 'array' or 'heap'.")
                    structure_choice = input("Input type of data structure (array, heap) you want to use: ")

        elif user_choice == 2:
            print("Solution for Ballyskate problem: ")
            file = "data/heap/ballyskate_layout.txt"
            graph = convert_to_adj_list(file)
            print("Distance and the shortest path from node 1 to node p is: ", tarjanstpath(graph, '1', 'p'))

        elif user_choice == 3:
            print("Solution for Padgett Marriage Alliances problem:")
            FloretineMarriage()

        else:
            print("Please choose 1, 2, or 3.")

        print("Shortest path program")
        print("1. Implementation of algorithms for large graph \n2. Solve Ballyskate problem \n"
              "3. Solve Padgett Marriage Alliances \n4. Quit")
        user_choice = int(input("Please select your choice: 1, 2, or 3.\n"))

    print("Thank you!")


if __name__ == "__main__":
    main()