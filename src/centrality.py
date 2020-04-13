from src.tarjan import tarjanspathtree
from src.ultilities import convert_to_adj_list, convert_to_graph
import networkx as nx


def closeness(graph):

    closeness_dict = {}

    for node_u in graph.keys():

        spath = tarjanspathtree(graph, node_u)
        connected_node = spath.keys()
        sum_of_distance = 0

        for node_v in connected_node:
            distance = spath[node_v][0]
            sum_of_distance += distance

        if sum_of_distance == 0:
            closeness_dict[node_u] = sum_of_distance
        else:
            closeness_dict[node_u] = (len(graph.keys()) - 2) * 1 / sum_of_distance

    return closeness_dict


def betweeness(graph):

    bw_dict = nx.betweenness_centrality(graph, normalized=True)

    return bw_dict


def degree(graph):

    deg_dict = nx.degree_centrality(graph)

    return deg_dict


def eigen_vector(graph):

    eig_dict = nx.eigenvector_centrality(graph)

    return eig_dict


def FloretineMarriage():

    txt_input_file = "data/padgett.txt"

    adj_list = convert_to_adj_list(txt_input_file)
    graph = convert_to_graph(txt_input_file)

    print("Centrality measures available: (1) degree, (2) eigenvector, (3) closeness, (4) and betweeness.")
    measure_choice = int(input("Please choose measures you want to calculate (from 1 to 4) \n"))

    while measure_choice:

        if measure_choice == 1:
            deg_dict = degree(graph)
            for node in deg_dict.keys():
                print("Degree centrality of node ", node, " is: ", "{:.3f}".format(deg_dict[node]))

            choice = input("Do you want to calculate other measures?? (y/n): ")

            while choice.lower() != 'n':

                if choice == "y":
                    FloretineMarriage()

                else:
                    print("Please choose y or n")

                choice = input("Do you want to calculate other measures?? (y/n): ")

            break

        if measure_choice == 2:
            eig_dict = eigen_vector(graph)
            for node in eig_dict.keys():
                print("Eigenvector centrality of node ", node, " is: ", "{:.3f}".format(eig_dict[node]))

            choice = input("Do you want to calculate other measures?? (y/n): ")

            while choice.lower() != 'n':

                if choice == "y":
                    FloretineMarriage()

                else:
                    print("Please choose y or n")

                choice = input("Do you want to calculate other measures?? (y/n): ")

            break

        if measure_choice == 3:
            closeness_dict = closeness(adj_list)
            for node in closeness_dict.keys():
                print("Closeness centrality of node ", node, " is: ", "{:.3f}".format(closeness_dict[node]))

            choice = input("Do you want to calculate other measures?? (y/n): ")

            while choice.lower() != 'n':

                if choice == "y":
                    FloretineMarriage()

                else:
                    print("Please choose y or n")

                choice = input("Do you want to calculate other measures?? (y/n): ")

            break

        if measure_choice == 4:
            bw_dict = betweeness(graph)
            for node in bw_dict.keys():
                print("Betweeness centrality of node ", node, " is: ", "{:.3f}".format(bw_dict[node]))

            choice = input("Do you want to calculate other measures?? (y/n): ")

            while choice.lower() != 'n':

                if choice == "y":
                    FloretineMarriage()

                else:
                    print("Please choose y or n")

                choice = input("Do you want to calculate other measures?? (y/n): ")

            break

        else:
            print("Please choose from 1 to 4")

        measure_choice = int(input("Please choose measures you want to calculate (from 1 to 4) \n"))


if __name__ == "__main__":
    FloretineMarriage()
