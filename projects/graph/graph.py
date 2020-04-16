"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} #adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph v1 to v2.
        """
        # Check if vertices exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            #print('Vertices', v1, v2)
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
            # May want to raise an exception (ValueError) here instead


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue and enqueue starting vertex
        qq = Queue()

        qq.enqueue([starting_vertex])
        # breakpoint()
        # Create a set of traversed vertices
        # using set instead of array is O(1) instead of O(n)
        # if the graph is huge and using an array will turn into O(n^2)
        visted = set()
        # While queue is not empty:
        while qq.size() > 0: # size is in util.py
            #dequeue/pop the first vertex
            path = qq.dequeue()
            # if not in visited
            if path[-1] not in visted:
                # DO THE THING!!! (search stop when you find something)
                print(path[-1]) #f"->BFT", 
                # Mark as visited
                visted.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path) #constructor built in python
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        NOT GUARANTEED TO GIVE SHORTEST PATH
        """
        # Create a stack and push(add) starting vertex
        ss = Stack()
        ss.push([starting_vertex]) #creates an array
        # Create a set of traversed vertices
        visited = set()
        # While stack is not empty
        while ss.size() > 0:
            # push/add the first index
            path = ss.pop()
            # if not in visited
            if path[-1] not in visited:
                # DO THE THING!! (search stop when you find something)
                print(path[-1]) #f"--->DFT", 
                # mark as visited
                visited.add(path[-1])
                # append/add all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    # makes copy 
                    new_path = list(path)
                    # adds the copy
                    new_path.append(next_vert)
                    ss.push(new_path)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        Pick a neighbor explaination (:20)
        binary search tree code
        """
        # Starting out with visited defaulting to None
        # it will turn into a recursion error if not done this way
        # Initial case
        if visited is None:
            visited = set()
        # Check if vertex (node) is visited
        # if not ...
        if starting_vertex not in visited:
            #  Tracking visited neighbors mark as visited
            visited.add(starting_vertex)
            # DO THE THING!! (search stop when you find something)
            print(starting_vertex) #f"---->DFT Recursion: ",
            # recurse all neighbors
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)
            # Base case: when all neighbors are visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

        """
        # Create a queue and enqueue starting vertex
        qq = Queue()
        # Enqueues the starting vertex
        qq.enqueue([starting_vertex]) # creates an array
        # Create a set to store the vertices
        visited = set()
        # While the queue is not empty
        while qq.size() > 0:
            # dequeue the first path
            #Since creating a path, order matters
            path = qq.dequeue()
            # grab the vertex from the end of the path
            vertex = path[-1]
            # check if it's been visited
            # if it hasn't been
            if vertex not in visited:
                # mark as visited
                visited.add(vertex)
                # check if it is the "target"
                if vertex == destination_vertex:
                    # if it is, return the path
                    return path
                # enqueue a path to all neighbors
                for neighbor in self.get_neighbors(vertex):
                    #make a copy of the path
                    new_path = list(path) #constructor built in python
                    # adds the copy
                    new_path.append(neighbor)
                    qq.enqueue(new_path)
        # Path not found
        #return None
        #return "Error path not found"
                


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack and push (add) the starting vertex
        ss = Stack()
        # Pushes (adds) the vertex
        ss.push([starting_vertex])
        # Create a visited set to store the vertices
        visited = set()
        # While the stack is not empty
        while ss.size() > 0:
            # pop the first path
            path = ss.pop()
            # grab the vertex from the end of the path
            vertex = path[-1]
            # check if visited
            # if it hasn't been visited
            if vertex not in visited:
                # mark as visited
                visited.add(vertex)
                # check if it is the "target"
                if vertex == destination_vertex:
                    # if it is, return the path
                    return path
                # push (add) path to all neighbors
                for neighbor in self.get_neighbors(vertex):
                    # make a copy of the path
                    new_path = list(path)
                    # add the copied path to the neighbor
                    new_path.append(neighbor)
                    #  add/push the new_path to the vertex
                    ss.push(new_path)
                


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Starting out with visited defaulting to None
        if visited is None:
            # returns an empty set
            visited = set()
        
        # Start the path with default of None
        if path is None:
            # The path will then return an empty list
            path = []
            
        # Check if vertex (node) has been visited
        if starting_vertex not in visited:
            visited.add(starting_vertex) 
            # make a copy of the path
            new_path = list(path)
            #or can use
            #path = path + [starting_vertex] and won't need line 228
            # add the copied path to the starting_vertex
            new_path.append(starting_vertex)
            # Checks if the starting_vertex and destination_vertex are the same
            if starting_vertex == destination_vertex:
                # if it is, then return the new_path
                return new_path
            for neighbor in self.get_neighbors(starting_vertex):
                new_dfs_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                if new_dfs_path is not None:
                    return new_dfs_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
