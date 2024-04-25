# <-- Python3.8.5 -->


from itertools import product
from typing import List, Tuple
from copy import deepcopy
import sympy


class GraphHelper:
    """Service class for working with graphs"""

    @staticmethod
    def AdjacencyToIncidenceMatrix(
        adjMatrix: List[List[int]], dimension: Tuple[int, int]
    ) -> List[List[int]]:
        """_summary_

        Args:
            adjMatrix (List[List[int]]): adjencity matrix
            dimension (Tuple[int, int]): dimensions

        Returns:
            List[List[int]]: incidence matrix
        """

        def __initIncidenceMatrix(_dimension: Tuple[int, int]) -> List[List[int]]:

            # Creating of zeros-matrix
            matrix = []

            for i in range(_dimension[0]):
                matrixString = []

                for j in range(_dimension[1]):
                    matrixString.append(0)

                matrix.append(matrixString)

            return matrix

        def __fillingIncidentMatrix(
            matrixBase: List[List[int]], adjMatrix: List[List[int]]
        ) -> List[List[int]]:
            # Convert an adjMatrix to incidence
            dCounter = 0

            for i in range(len(adjMatrix)):
                for j in range(i, len(adjMatrix[i])):
                    for _ in range(adjMatrix[i][j]):
                        if i == j:
                            matrixBase[i][dCounter] = 1
                        else:
                            matrixBase[i][dCounter] = 1
                            matrixBase[j][dCounter] = 1

                        dCounter += 1

            return matrixBase

        return __fillingIncidentMatrix(
            matrixBase=__initIncidenceMatrix(dimension), adjMatrix=adjMatrix
        )

    @staticmethod
    def IncidenceToAdjacencyMatrix(incMatrix: List[List[int]]) -> List[List[int]]:
        """_summary_

        Args:
            incMatrix (List[List[int]]): _description_

        Returns:
            List[List[int]]: _description_
        """
        dimension: int = len(incMatrix)

        def __initAdjacencyMatrix(dimension: int) -> List[List[int]]:
            # Creating of zeros-matrixs
            matrix = []

            for i in range(dimension):
                matrixString = []

                for j in range(dimension):
                    matrixString.append(0)
                matrix.append(matrixString)

            return matrix

        def __fillingAdjacencyMatrix(
            matrixBase: List[List[int]], incMatrix: List[List[int]]
        ) -> List[List[int]]:
            # Convert an adjMAtrix to incident
            for i in range(len(incMatrix[0])):
                linkedEdges: List[int] = []

                for j in range(len(incMatrix)):
                    if incMatrix[j][i] == 1:
                        linkedEdges.append(j)
                if len(linkedEdges) != 1:
                    matrixBase[linkedEdges[0]][linkedEdges[1]] += 1
                else:
                    matrixBase[linkedEdges[0]][linkedEdges[0]] += 1

                for i in range(1, len(matrixBase)):
                    for j in range(i):
                        matrixBase[i][j] = matrixBase[j][i]

            return matrixBase

        return __fillingAdjacencyMatrix(
            matrixBase=__initAdjacencyMatrix(dimension=dimension), incMatrix=incMatrix
        )

    @staticmethod
    def MultiplicationMatrix(matrixOne, matrixTwo):
        rowOne = len(matrixOne)
        columnOne = len(matrixOne[0])
        rowTwo = len(matrixTwo)
        columnTwo = len(matrixTwo[0])
        if columnOne == rowTwo:
            result = [[0 for _ in range(columnTwo)] for _ in range(rowOne)]
            for row in range(rowOne):
                for column in range(columnTwo):
                    for j in range(columnOne):
                        result[row][column] += matrixOne[row][j] * matrixTwo[j][column]
            return result
        else:
            return None

    @staticmethod
    def powerMatrix(matrix, degree):
        if len(matrix) != len(matrix[0]):
            return None
        else:
            result = deepcopy(matrix)
            for i in range(degree - 1):
                result = GraphHelper.MultiplicationMatrix(result, matrix)
            return result

    @staticmethod
    def AdjacencyMatrixToList(matrix):
        adjacencyMatrix = dict()
        for i, node in enumerate(matrix):
            adjacents = []
            for j, isConnect in enumerate(node):
                if isConnect:
                    adjacents.append(j)
            adjacencyMatrix[i] = adjacents
        return adjacencyMatrix

    @staticmethod
    def createGraphSkeletonMatrix(adjMatrix):
        skeletonMatrix = [
            [0 for i in range(len(adjMatrix))] for _ in range(len(adjMatrix))
        ]
        for i, j in product(range(len(adjMatrix)), repeat=2):
            if i == j:
                skeletonMatrix[i][j] = 0
            elif adjMatrix[i][j]:
                skeletonMatrix[i][j] = 1

        return skeletonMatrix

    @staticmethod
    def createDeviationMatrix(adjMatrix):
        deviationMatrix = [
            [0 for _ in range(len(adjMatrix))] for i in range(len(adjMatrix))
        ]
        n = len(adjMatrix)
        k = 1
        S = deepcopy(adjMatrix)
        for i in range(n):
            S[i][i] = 1
        S2 = deepcopy(S)

        deviationMatrixOld = deepcopy(deviationMatrix)

        while True:
            isDeviationMatrixFull = True
            for i in range(n):
                for j in range(i + 1, n):
                    if S2[i][j] != 0 and deviationMatrix[i][j] == 0:
                        deviationMatrix[i][j] = k
                        deviationMatrix[j][i] = k
            k += 1

            for i in range(n):
                for j in range(i + 1, n):
                    if deviationMatrix[i][j] == 0:
                        isDeviationMatrixFull = False
                        break

            isSameMatrix = False
            if deviationMatrix == deviationMatrixOld:
                isSameMatrix = True

            if isDeviationMatrixFull == True or isSameMatrix == 1:
                break

            S2 = GraphHelper.powerMatrix(S, k)
            deviationMatrixOld = deepcopy(deviationMatrix)

        for i in range(n):
            for j in range(i + 1, n):
                if deviationMatrix[i][j] == 0:
                    deviationMatrix[i][j] == -1
                    deviationMatrix[i][j] == -1

        return deviationMatrix

    @staticmethod
    def getDeviationSpecifications(deviationMatrix):
        radius: int
        diameter: int
        peripherals: List[int]
        centrals: List[int]
        weights: List[int]

        weights = []
        centrals = []
        peripherals = []

        for row in deviationMatrix:
            weights.append(max(row))

        radius = min(weights)
        diameter = max(weights)

        for row in range(len(deviationMatrix)):
            if diameter <= max(deviationMatrix[row]):
                centrals.append(row)
            elif diameter >= max(deviationMatrix[row]):
                peripherals.append(row)

        return radius, diameter, peripherals, centrals

    """    @staticmethod
    def AdjacencySkeletonMatrix(adjMatrix):
        skeleton = [[0 for _ in range(len(adjMatrix))] for i in range(len(adjMatrix))]

        for i in range(len(adjMatrix)):
            for j in range(len(adjMatrix)):
                if adjMatrix[i][j] > 0:
                    skeleton[i][j] = 1

        return skeleton"""

    @staticmethod
    def CountEdges(
        adjMatrix: List[List[int]], graphType: int
    ) -> int:  # Counting of edges
        dSum: int = 0

        if graphType != 3:
            for matrString in adjMatrix:
                dSum += sum(matrString)

            dSum //= 2
        else:
            dMainDiagSum: int = 0

            for i in range(len(adjMatrix)):
                for j in range(len(adjMatrix)):
                    if i == j:
                        dMainDiagSum += adjMatrix[i][j]
                        continue
                    else:
                        dSum += adjMatrix[i][j]

            dSum //= 2
            dSum += dMainDiagSum

        return dSum

    @staticmethod
    def createAddForAdjacency(adjMatrix):
        addAdjMatrix = [
            [0 for i in range(len(adjMatrix))] for _ in range(len(adjMatrix))
        ]

        for i in range(len(adjMatrix)):
            for j in range(len(adjMatrix)):
                if i != j:
                    addAdjMatrix[i][j] = 1 if adjMatrix[i][j] == 0 else 0
        return addAdjMatrix

    @staticmethod
    def MaguWaissmann(adjMatrix):
        skeletonAdjacencyMatrix = GraphHelper.createGraphSkeletonMatrix(
            adjMatrix=adjMatrix
        )
        # addMatrixSkeleton = GraphHelper.createAddForAdjacency(skeletonAdjacencyMatrix)

        countEdges = GraphHelper.CountEdges(
            adjMatrix=skeletonAdjacencyMatrix, graphType=0
        )

        skeletonIncidenceMatrix = GraphHelper.AdjacencyToIncidenceMatrix(
            adjMatrix=skeletonAdjacencyMatrix, dimension=(len(adjMatrix), countEdges)
        )

        X = []

        for num in range(len(skeletonIncidenceMatrix)):
            X.append(sympy.Symbol(f"x{num}"))

        for i in range(len(skeletonIncidenceMatrix)):
            for j in range(len(skeletonIncidenceMatrix[0])):
                skeletonIncidenceMatrix[i][j] = skeletonIncidenceMatrix[i][j] * X[i]

        polynom = []

        for j in range(len(skeletonIncidenceMatrix[0])):
            s = 0
            for i in range(len(skeletonIncidenceMatrix)):
                if skeletonIncidenceMatrix[i][j] != 0:
                    s += skeletonIncidenceMatrix[i][j]
            polynom.append(s)

        mPolynom = 1

        for expr in polynom:
            mPolynom *= expr

        cliques = []
        mPolynom = sympy.expand(mPolynom)

        for i in mPolynom.args:
            dClique = []
            for j in i.args:
                if sympy.degree(j) != 0:
                    vertex = sympy.powdenest(j ** (1 / sympy.degree(j)), force=True)
                    dClique.append(vertex)
            cliques.append(dClique)

        emptySubgraphs = []
        for i in cliques:
            subgraph = []
            for vertex in X:
                if vertex not in i:
                    subgraph.append(vertex)
            if subgraph not in emptySubgraphs:
                emptySubgraphs.append(subgraph)

        return emptySubgraphs

    @staticmethod
    def findMaxEmptySubgraphs(adjMatrix):
        subgraphs = GraphHelper.MaguWaissmann(adjMatrix=adjMatrix)
        maxLen = 0
        maxSg = []

        for sg in subgraphs:
            if len(sg) >= maxLen:
                maxLen = len(sg)
        

        return maxSg

    @staticmethod
    def findMaxCompleteSubgraphs(adjMatrix):
        addAdjMatrix = GraphHelper.createAddForAdjacency(adjMatrix=adjMatrix)
        subgraphs = GraphHelper.MaguWaissmann(adjMatrix=addAdjMatrix)
        maxLen = 0
        maxSg = []

        for sg in subgraphs:
            if len(sg) >= maxLen:
                maxLen = len(sg)
                maxSg = sg

        return maxSg

    @staticmethod
    def getChromaticNumber(adjMatrix):
        subgraphs = GraphHelper.MaguWaissmann(adjMatrix=adjMatrix)
        colors = 0
        visited = []

        for sg in subgraphs:
            dSg = deepcopy(sg)
            for vertex in dSg:
                if vertex in visited:
                    sg.remove(vertex)
                else:
                    visited.append(vertex)
            if sg:
                colors += 1
        return colors
    
    @staticmethod
    def colorizeGraph(adjMatrix):
        dim = len(adjMatrix)
        colors = [0 for _ in range(dim)]
        for i in range(dim):
            unavailableColors = []
            for j in range(dim):
                if(adjMatrix[i][j] >= 1 and colors[j] != 0):
                    unavailableColors.append(colors[j])
            color = 1
            
            while color in unavailableColors:
                color+=1
            colors[i] = color
            
        colorizedVertexes = {vertex:colors[vertex] for vertex in range(dim)}
        
        return colorizedVertexes
