# <-- Python3.8.5 -->


from itertools import product
from typing import List, Tuple
import copy


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
            # Convert an adjMAtrix to incident
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
    def powerMatrix(matrix, degree):

        __dMatrix = [[0 for i in range(len(matrix))] for _ in range(len(matrix))]
        dMatrix = copy.deepcopy(matrix)

        for _ in range(degree - 1):
            for i, j in product(range(len(matrix)), repeat=2):
                dElem = 0
                for k in range(len(matrix)):
                    dElem += dMatrix[i][k] * matrix[k][j]
                __dMatrix[i][j] = dElem
            dMatrix = copy.deepcopy(__dMatrix)

        dMatrix = __dMatrix
        return dMatrix

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
    def createMetricMatrix(adjMatrix):
        __skeletonMatrix = GraphHelper.createGraphSkeletonMatrix(adjMatrix=adjMatrix)
        
        
