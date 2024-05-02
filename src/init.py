# <-- Python3.8.5 -->


from os import system
from GraphVisualizer import GraphVisualizer
from MathGraph import MathGraph
from Helpers import GraphHelper
from time import sleep


def main(*args, **kwargs) -> None:
    # Clear the consol
    system("cls")

    print(f"Graphs, v1.0\n{'*'*12}")
    sleep(3)

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
5. Simple weighted digraph

Form of request: dimension type isDijkstra[1/0]
Example: 3 2 1-> 3-dim multiple graph (use Dijkstra)
"""
        )

        try:
            dimension, graphType, isDijkstra = map(int, input(">>>  ").split())
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
        print()

        print("Deviation Matrix")
        for i in graph.DeviationMatrix:
            print(i)
        print()

        print("Radius, diameter")
        for i in (graph.Radius, graph.Diameter):
            print(i, end=", ")
        print(end="\n\n")

        print("Centrals")
        for i in graph.CentralVertexes:
            print(i, end=" ")
        print(end="\n\n")

        print("Peripherals")
        for i in graph.PeripheralVertexes:
            print(i, end=" ")
        print(end="\n\n")

        print("Max completed subgraphs")
        print(graph.MaxCompleteSubgraphs)
        print(end="\n\n")

        print("Chromatic number")
        print(graph.ChromaticNumber)
        print(end="\n\n")

        print("Colorizing")
        print(graph.ColorizedVertexes)
        for i in range(len(graph.ColorizedVertexes)):
            print(f"v{i}:{graph.ColorizedVertexes[i]}")
        print(end="\n\n")

        if isDijkstra == 1:
            print("Dijkstra Algorithm")
            start, end = map(int, input("Please, enter a start and end>>>   ").split())
            res = GraphHelper.DijkstraAlgorhitm(graph.AdjacencyMatrix, start, end)
            print(
                f"Start vertex:{res[0]}\nEnd vertex:{res[1]}\nPath:{res[3]}\nLength of path:{res[2]}\n"
            )

        GraphVisualizer.Visualize(
            graph.AdjacencyMatrix,
            graph.ColorizedVertexes,
            graph.ChromaticNumber,
            graphType - 1,
        )

        del graph

        # Clear a console
        system("cls")


if __name__ == "__main__":
    main()
