import time
import sys

# Set a higher recursion limit for potentially large graphs, useful for backtracking algorithms.
# Uncomment the line below if you encounter a RecursionError for large inputs.
# sys.setrecursionlimit(2000)

def is_safe(v, graph, color, c):
    """
    Checks if assigning color 'c' to vertex 'v' is safe.
    It is safe if no adjacent vertex 'u' already has color 'c'.

    Args:
        v (int): The current vertex index (0 to N-1).
        graph (list of list of int): Adjacency matrix representation of the graph.
        color (list of int): Array storing the color assigned to each vertex so far.
        c (int): The color we are trying to assign (1 to m).

    Returns:
        bool: True if the color assignment is valid, False otherwise.
    """
    # Iterate through all vertices 'u' (0 to N-1)
    for u in range(len(graph)):
        # Check if 'v' and 'u' are adjacent (graph[v][u] == 1)
        # AND if 'u' already has the color 'c' (color[u] == c)
        if graph[v][u] == 1 and color[u] == c:
            return False
    return True

def graph_coloring_util(m, graph, color, v):
    """
    A recursive utility function to solve the graph coloring problem using backtracking.

    Args:
        m (int): The maximum number of colors allowed.
        graph (list of list of int): Adjacency matrix.
        color (list of int): Current color assignments (will be modified in-place).
        v (int): The current vertex being considered (index 0 to N-1).

    Returns:
        bool: True if a valid coloring is found starting from vertex 'v', False otherwise.
    """
    N = len(graph)

    # Base case: If all vertices are colored, return True
    if v == N:
        return True

    # Try assigning colors 1 through m to the current vertex 'v'
    for c in range(1, m + 1):
        if is_safe(v, graph, color, c):
            # 1. Assign color 'c' to vertex 'v'
            color[v] = c

            # 2. Recurse to the next vertex (v + 1)
            if graph_coloring_util(m, graph, color, v + 1):
                return True

            # 3. Backtrack: If assigning color 'c' didn't lead to a solution,
            #    un-assign the color (reset to 0) and try the next color.
            color[v] = 0

    # If no color can be assigned to this vertex, return False
    return False

def graph_coloring(graph, m):
    """
    Main function to solve the M-coloring problem.

    Args:
        graph (list of list of int): Adjacency matrix of the graph.
        m (int): Maximum number of colors allowed.
    """
    N = len(graph) # Number of vertices
    # Initialize color array. color[i] will store the color of vertex i. 0 means uncolored.
    color = [0] * N

    print(f"--- Graph Coloring Solver (M={m}) ---")
    print(f"Graph with {N} vertices and {m} colors maximum.")

    start_time = time.time()

    if not graph_coloring_util(m, graph, color, 0):
        print("\nSolution Not Found:")
        print(f"The graph cannot be colored using {m} colors.")
        return False

    end_time = time.time()

    # If the utility function returns True, a solution is found
    print("\nSolution Found:")
    print(f"Coloring (Vertex Index -> Color Index [1 to {m}]):")
    for i in range(N):
        print(f"  Vertex {i}: Color {color[i]}")

    print(f"\nTime taken: {end_time - start_time:.6f} seconds")
    return True

def get_user_input_graph():
    """
    Interactively prompts the user for the graph structure and number of colors.
    """
    # Get number of vertices (N)
    while True:
        try:
            N = int(input("Enter the number of vertices (N): "))
            if N <= 0:
                print("Number of vertices must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Get maximum number of colors (M)
    while True:
        try:
            M = int(input(f"Enter the maximum number of colors (M): "))
            if M <= 0:
                print("Number of colors must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Get adjacency matrix
    print(f"\nNow enter the {N}x{N} Adjacency Matrix (0 for no edge, 1 for edge):")
    graph = []
    for i in range(N):
        while True:
            try:
                row_str = input(f"Enter row {i} (space-separated 0s and 1s): ")
                row = [int(x) for x in row_str.split()]

                if len(row) != N:
                    print(f"Row must contain exactly {N} values. Try again.")
                    continue

                # Basic validation for 0/1 inputs
                if not all(x in [0, 1] for x in row):
                    print("Invalid input. Matrix entries must be 0 or 1.")
                    continue

                graph.append(row)
                break
            except ValueError:
                print("Invalid input format. Please ensure all inputs are space-separated numbers.")
            except Exception as e:
                print(f"An unexpected error occurred during row input: {e}")

    return graph, M

# --- Main execution block for interactive mode ---
if __name__ == "__main__":
    try:
        # Prompt user for graph data
        input_graph, input_m = get_user_input_graph()

        # Solve the graph coloring problem
        graph_coloring(input_graph, input_m)

    except Exception as e:
        # Catch unexpected errors during execution
        print(f"\nAn unexpected error occurred: {e}")
        print("Please ensure your graph input was correctly formatted.")