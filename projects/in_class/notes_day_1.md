https://youtu.be/X3WQa9TQonY- Day 1 graphs

Graphs
------
Nodes == Verts == Vertices == Vertexes
   The thing that stores the data
Nodes connected by Edges
   Edges can be directional
If a graph has directional edges, it's called a "directed graph".
Traversals
----------
Keep track of what nodes have been visited to avoid revisiting them
   * Visited flag
   * Hash Table
   * Set
Depth-First Traversal
---------------------
    Push starting node on stack
    while stack isn't empty:
        pop the node off the top of the stack
        if node isn't visited:
            visit the node (e.g. print it out)
            mark it as visited
            push all its neighbors on the stack
Breadth-First Traversal
-----------------------
    Add starting node to queue
    while queue isn't empty:
        take the node from the front of the queue
        if node isn't visited:
            visit the node (e.g. print it out)
            mark it as visited
            add all its neighbors to the queue
Graph Representations
---------------------
How we store the graph in memory
1. Adjacency matrix
2. Adjacency list
Matrix:
A matrix is a grid. Keep track of which nodes connect to others.
  A B C D E F G H    To
A   T   T       T
B     T
C   T         T
D T
E
F
G     T
H T
From
List:
Keep list of nodes this one is connected to
A [B H D]
B [C A F E]
C [B G]
D [A]
E [B]
F [B]
G [C H]
H [G A]
Breadth First Search
--------------------
Same as a traveral, but we want to:
* Find a node
* Find the shortest path to that node
def bfs(self, starting_vertex_id, target_vertex_id):
    # Create an empty queue and enqueue A PATH TO the starting vertex ID
    # Create a Set to store visited vertices
    # While the queue is not empty...
        # Dequeue the first PATH
        # Grab the last vertex from the PATH
        # If that vertex has not been visited...
            # CHECK IF IT'S THE TARGET
              # IF SO, RETURN PATH
            # Mark it as visited...
            # Then add A PATH TO its neighbors to the back of the queue
              # COPY THE PATH
              # APPEND THE NEIGHOR TO THE BACK
--------------------------
A hash table that just stores True/False values is equivalent to a Set.