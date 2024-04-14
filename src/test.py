def matrixToList(matrix):
    graph = dict()
    for i, node in enumerate(matrix):
        adj = []
        for j, con in enumerate(node):
            if con:
                adj.append(j)
        graph[i] = adj
    return graph






import Helpers

sss = -1

print(bool(0))