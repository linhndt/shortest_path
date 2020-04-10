import numpy as np


def startwith(start: int, matrix: list) -> list:
    # param start: index of starting point, starts from 0
    # param matrix: adjacency matrix
    # return to a list
    permanent_vertices = [start]
    # store the points of which the shortest distance has been determined
    temporary_vertices = [x for x in range(len(matrix)) if x != start]
    # store the points of which the shortest distance has not been determined
    dis = matrix[start]
    # result to be returned
    # initialization

    # determine the next point with shortest distance

    while len(temporary_vertices):
        idx = temporary_vertices[0]
        for i in temporary_vertices:
            if dis[i] < dis[idx]:
                idx = i
        # traverse the temporary_vertices and find the points with the shortest distance

        temporary_vertices.remove(idx)
        permanent_vertices.append(idx)
        # points with the shortest distance move from list temporary_vertices to list permanet_vertices

        for i in temporary_vertices:
            if dis[idx] + matrix[idx][i] < dis[i]:
                dis[i] = dis[idx] + matrix[idx][i]
            # Based on idx, check the distance from idx to other points.
            # If the distance from start point to idx,
            # then to point n is less than the distance from start point to point n, update the value of dis [n]

    return dis
    # repeat the above process until terporary_vertices is empty


if __name__ == "__main__":
    matrix = np.loadtxt('../data/array/ballyskate_layout.txt', skiprows=2, dtype=int)
    # load the txt file with adjacency matrix

    dis = startwith(0, matrix)

    print(dis)