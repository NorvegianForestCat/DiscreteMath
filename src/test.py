def f(adjMatrix):
    edges: int = 0
    for i in range(len(adjMatrix)):
        for j in range(i, len(adjMatrix)):
            edges+=adjMatrix[i][j]
    print(edges)
    vertex = len(adjMatrix)
    incMatrix = [[0 for i in range(edges)] for _ in range(vertex)]
    print(incMatrix)
    
    for i in range(len(adjMatrix)):
        for j in range(i, len(adjMatrix[i])):
            for _ in range(adjMatrix[i][j]):
                if i == j:
                    incMatrix[i][dCounter] = 1
                else:
                    incMatrix[i][dCounter] = 1
                    incMatrix[j][dCounter] = 1

                dCounter += 1
m = [
    [1, 4, 1],
    [4, 1, 0],
    [1, 0, 0],
    ]
f(m)
