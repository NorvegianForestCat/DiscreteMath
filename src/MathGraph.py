# <-- Python3.8.5 -->


from typing import List, Tuple
from Helpers import GraphHelper

import random


class MathGraph:
    """
    Class for Mathematical interpretation of graphs

    Properties:
        IncidenceMatrix (int): returns a incidence matrix
        AdjacencyMatrix (int): returns a adjacency matrix
        EdgeCount (int): returns a number of edges
        VertexCount (int): returns a number of nodes
    """

    __nodeCount: int
    __edgeNumber: int
    __radius: int
    __diameter: int
    __adjacencyMatrix: List[List[int]]
    __incidenceMatrix: List[List[int]]
    __deviationMatrix: List[List[int]]
    __graphTypes: List[int]
    __peripheralVertexes: List[int]
    __centralVertexes: List[int]
    __maxCompleteSubgraphs: List[List[int]]
    __maxEmptySubgraphs: List[List[int]]
    __colorizing: List[int]
    __chromaticNum: int

    __maxEdgeCount: int = 5

    def __init__(self, dimension: int = 3, graphType: int = 0) -> None:
        """
        Args:
            dimension (int, optional): Number of dimensions. Defaults to 3.
            graphType (int, optional): Type of graph (0-3). Defaults to 0.
        """
        self.__nodeCount = dimension
        self.__adjacencyMatrix = self.__createAdjacencyMatrix(
            dimension=dimension, mode=graphType
        )
        self.__edgeNumber = self.__countEdges(
            adjMatrix=self.AdjacencyMatrix, graphType=graphType
        )
        self.__incidenceMatrix = self.__createIncidenceMatrix(
            dimension=(self.__nodeCount, self.__edgeNumber),
            adjMatrix=self.AdjacencyMatrix,
        )
        self.__deviationMatrix = GraphHelper.createDeviationMatrix(
            adjMatrix=self.AdjacencyMatrix
        )
        (
            self.__radius,
            self.__diameter,
            self.__peripheralVertexes,
            self.__centralVertexes,
        ) = GraphHelper.getDeviationSpecifications(self.DeviationMatrix)

        if graphType != 4:
            self.__maxEmptySubgraphs = GraphHelper.findMaxEmptySubgraphs(
                adjMatrix=self.AdjacencyMatrix
            )
            self.__maxCompleteSubgraphs = GraphHelper.findMaxCompleteSubgraphs(
                adjMatrix=self.AdjacencyMatrix
            )
        else:
            self.__maxEmptySubgraphs = None
            self.__maxCompleteSubgraphs = None
        self.__colorizing = GraphHelper.colorizeGraph(adjMatrix=self.AdjacencyMatrix)
        self.__chromaticNum = GraphHelper.getChromaticNumber(
            adjMatrix=self.AdjacencyMatrix
        )

    def __format_simpleGraph(
        self, i: int, j: int
    ) -> int:  # Simple graph adjMatrix form
        if i != j:
            return random.randint(0, 1)
        else:
            return 0

    def __format_fullGraph(self, i: int, j: int) -> int:  # Full graph adjMatrix form
        if i != j:
            return 1
        else:
            return 0

    def __format_multigraph(self, i: int, j: int) -> int:  # Multigraph adjMatrix form
        if i != j:
            return random.randint(0, self.__maxEdgeCount)
        else:
            return 0

    def __format_withLoops(
        self, i: int, j: int
    ) -> int:  # Graph with loops adjMatrix form
        return random.randint(0, self.__maxEdgeCount)

    def __format_orientedSimpleWeightGraph(self, i, j):
        if i != j:
            return random.randint(0, 5)
        else:
            return 0

    # Graph types
    __graphTypes = [
        __format_simpleGraph,
        __format_fullGraph,
        __format_multigraph,
        __format_withLoops,
        __format_orientedSimpleWeightGraph,
    ]

    def __countEdges(
        self, adjMatrix: List[List[int]], graphType: int
    ) -> int:  # Counting of edges
        dSum: int = 0

        if graphType != 3 and graphType < 4:
            for matrString in adjMatrix:
                dSum += sum(matrString)

            dSum //= 2
        elif graphType == 4:
            dmatrix = GraphHelper.createGraphSkeletonMatrix(adjMatrix=adjMatrix)
            for matrString in dmatrix:
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

    def __createAdjacencyMatrix(
        self, dimension: int, mode: int
    ) -> List[List[int]]:  # Creating an adjMatrix

        def __initAdjacencyMatrix(
            dimension: int,
        ) -> List[List[int]]:  # Creating xeros-matrix
            matrix = []

            for i in range(dimension):
                matrixString = []
                for j in range(dimension):
                    matrixString.append(0)
                matrix.append(matrixString)

            return matrix

        def __fillingAdjacencyMatrix(
            matrix: List[List[int]], mode: int
        ) -> List[List[int]]:  # Filling zeros-matrix
            if mode != 4:
                for i in range(len(matrix)):
                    for j in range(len(matrix[i]) - i):
                        matrix[i][j + i] = self.__graphTypes[mode](self, i=i, j=j + i)

                for i in range(1, len(matrix)):
                    for j in range(i):
                        matrix[i][j] = matrix[j][i]
            else:
                for i in range(len(matrix)):
                    for j in range(len(matrix)):
                        matrix[i][j] = self.__graphTypes[mode](self, i, j)

            return matrix

        return __fillingAdjacencyMatrix(__initAdjacencyMatrix(dimension), mode)

    def __createIncidenceMatrix(
        self, dimension: Tuple[int, int], adjMatrix: List[List[int]]
    ) -> List[List[int]]:  # Creating incMatrix

        return GraphHelper.AdjacencyToIncidenceMatrix(
            adjMatrix=adjMatrix, dimension=dimension
        )

    @property
    def IncidenceMatrix(self) -> List[List[int]]:
        """Incidence matrix

        Returns:
            List[List[int]]: incidence matrix
        """
        return self.__incidenceMatrix

    @property
    def AdjacencyMatrix(self) -> List[List[int]]:
        """Adjacency matrix

        Returns:
            List[List[int]]: adjacency matrix
        """
        return self.__adjacencyMatrix

    @property
    def EdgeCount(self) -> int:
        """Edges count

        Returns:
            int: edges count
        """
        return self.__edgeNumber

    @property
    def VertexCount(self) -> int:
        """Nodes count
        Returns:
            int: nodes (vertex) count
        """
        return self.__nodeCount

    @property
    def DeviationMatrix(self) -> List[List[int]]:
        """_summary_

        Returns:
            List[List[int]]: _description_
        """
        return self.__deviationMatrix

    @property
    def Radius(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__radius

    @property
    def Diameter(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__diameter

    @property
    def PeripheralVertexes(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__peripheralVertexes

    @property
    def CentralVertexes(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__centralVertexes

    @property
    def MaxCompleteSubgraphs(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__maxCompleteSubgraphs

    @property
    def MaxEmptySubgraphs(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__maxEmptySubgraphs

    @property
    def ColorizedVertexes(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__colorizing

    @property
    def ChromaticNumber(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__chromaticNum
