import sys
from typing import List, Dict, Optional

# Set recursion limit higher for complex graphs
sys.setrecursionlimit(2000)

def is_safe(v: int, graph: List[List[int]], color: List[int], c: int, V: int) -> bool:
    """
    Checks if assigning color 'c' to vertex 'v' is safe.
    It is safe if no adjacent vertex 'i' currently has color 'c'.

    :param v: The current vertex index (0 to V-1).
    :param graph: The V x V adjacency matrix.
    :param color: The list of colors assigned to vertices so far.
    :param c: The color being tested (1 to k).
    :param V: Total number of vertices.
    :return: True if the color assignment is valid, False otherwise.
    """
    for i in range(V):
        # Check if 'v' and 'i' are adjacent AND 'i' already has the color 'c'
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring_util(v: int, k: int, V: int, graph: List[List[int]], 
                        color: List[int], solutions: List[List[int]]) -> None:
    """
    Recursive backtracking utility function to find all k-colorings.

    :param v: The current vertex index to color.
    :param k: The number of colors available (k).
    :param V: Total number of vertices.
    :param graph: The V x V adjacency matrix.
    :param color: The current color assignment list (modified recursively).
    :param solutions: List to store all valid color assignment lists.
    """
    # Base Case: If all vertices are successfully colored, store the solution
    if v == V:
        solutions.append(list(color))
        return

    # Try all available colors (1 to k) for vertex 'v'
    for c in range(1, k + 1):
        if is_safe(v, graph, color, c, V):
            color[v] = c  # Assign the color
            
            # Recur for the next vertex (v + 1)
            graph_coloring_util(v + 1, k, V, graph, color, solutions)
            
            # Backtrack: Unassign the color before the next iteration
            # This is crucial for exploring other possible color assignments
            color[v] = 0

def solve_graph_coloring():
    """Main function to handle input, find the minimum chromatic number, and display results."""
    print("--- Graph Coloring Problem Solver (Backtracking) ---")
    
    try:
        # 1. Take number of vertices as input
        V = int(input("Enter the number of vertices (V): "))
        if V <= 0:
            print("Number of vertices must be positive.")
            return

        print(f"\n2. Enter the {V}x{V} Adjacency Matrix (0 or 1):")
        
        # 2. Accept adjacency matrix representation
        graph = []
        for i in range(V):
            row_input = input(f"Enter row {i+1} (space-separated {V} values): ").split()
            if len(row_input) != V:
                print(f"Error: Expected {V} values, got {len(row_input)}. Exiting.")
                return
            graph.append([int(x) for x in row_input])

        # Validate symmetry for an undirected graph
        for i in range(V):
            for j in range(V):
                if graph[i][j] != graph[j][i]:
                    print("Error: The matrix is not symmetric (required for undirected graph). Exiting.")
                    return
                if graph[i][j] not in (0, 1):
                    print("Error: Matrix must contain only 0s and 1s. Exiting.")
                    return

    except ValueError:
        print("\nInvalid input. Please ensure all inputs are correct numbers.")
        return
    except Exception as e:
        print(f"\nAn error occurred during input: {e}")
        return

    # 4. Find the minimum number of colors (Chromatic Number, χ(G))
    min_k = V
    min_solutions = []

    print("\n--- Solving ---")
    
    # Start checking for k=1 color up to V colors
    for k in range(1, V + 1):
        solutions = []
        # Initialize color array: 0 means uncolored
        color = [0] * V
        
        # Start coloring from the first vertex (index 0)
        graph_coloring_util(0, k, V, graph, color, solutions)
        
        if solutions:
            # If solutions are found for this 'k', it is the minimum required
            min_k = k
            min_solutions = solutions
            break

    # 4. Display results
    print("-" * 50)
    if not min_solutions:
        print("Could not find a valid coloring for this graph.")
        return

    print(f"Minimum Number of Colors Required (Chromatic Number, χ(G)): **{min_k}**")
    print(f"Number of distinct valid color assignments using {min_k} colors: {len(min_solutions)}")
    
    # Display all valid color assignments
    print("\nAll Valid Color Assignments (Vertex Index: Color):")
    for i, sol in enumerate(min_solutions):
        # Format the output for clarity
        assignment = {f'V{j+1}': sol[j] for j in range(V)}
        print(f"  Assignment {i+1}: {assignment}")

# Example Input (Graph from Q2, χ(G)=3):
# V=5
# Row 1: 0 1 1 0 0
# Row 2: 1 0 1 1 0
# Row 3: 1 1 0 0 1
# Row 4: 0 1 0 0 1
# Row 5: 0 0 1 1 0

if __name__ == "__main__":
    solve_graph_coloring()
