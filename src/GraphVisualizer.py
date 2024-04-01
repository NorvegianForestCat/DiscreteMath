# <-- Python3.8.5 -->


from typing import List, AnyStr, Dict, Tuple

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


class GraphVisualizer:
    """Static class for graph visualization

    Returns:
        Visualize (List[List[int]]) -> return None
            Static method for visualization
    """

    @staticmethod
    def Visualize(adjMatrix: List[List[int]]) -> None:

        def __getEdgeLabels(
            adjMatrix: List[List[int]],
        ) -> Dict[Tuple[int, int], AnyStr]:

            edge_labels: Dict[Tuple[int, int], AnyStr] = {}

            # Filling of labels dict
            for i in range(len(adjMatrix)):
                for j in range(i + 1, len(adjMatrix)):
                    degree = adjMatrix[i][j]

                    if degree != 0 and degree != 1:
                        edge_labels[(i, j)] = str(degree)

            return edge_labels

        # Graph show
        graph: object = nx.Graph(np.array(adjMatrix))
        edgeLabels = __getEdgeLabels(adjMatrix=adjMatrix)

        nx.draw(G=graph, pos=nx.circular_layout(graph), with_labels=True)
        nx.draw_networkx_edge_labels(
            G=graph, pos=nx.circular_layout(graph), edge_labels=edgeLabels
        )

        plt.show()
