# <-- Python3.8.5 -->


from os import system
from GraphVisualizer import GraphVisualizer
from MathGraph import MathGraph
from Helpers import GraphHelper


def main(*args, **kwargs) -> None:
    # Clear the consol
    system("cls")

    print(f"Graphs, v1.0\n{'*'*12}")

    # Variables
    iterFlag: bool = True
    graphType: int
    dimension: int

    # Endless cycle of requests
    while iterFlag:
        # Start text
        print(
            """
1. Simple 
2. Full
3. Multiple
4. With loops

Form of request: dimension type
Example: 3 2 -> 3-dim multiple graph
"""
        )

        try:
            dimension, graphType = map(int, input(">>>  ").split())
        except ValueError as error:
            break

        # Creatung graph and its showing
        graph: MathGraph = MathGraph(dimension=dimension, graphType=graphType - 1)

        print("Adjacency Matrix")
        for i in graph.AdjacencyMatrix:
            print(i)
        print()

        print("Incidence matrix")
        for i in graph.IncidenceMatrix:
            print(i)

        GraphVisualizer.Visualize(graph.AdjacencyMatrix)
        
        del graph

        # Clear a console
        system("cls")


if __name__ == "__main__":
    main()
