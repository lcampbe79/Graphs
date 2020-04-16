
#1. Translate the problem into graph terminology
#2. Build your graph
#3. Traverse your graph. 

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            #add row
            self.vertices[vertex_id] = set()
    
    #because of parent we add the directed edge
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #uses this because of add_vertex
        if v1 in self.vertices and v2 in self.vertices:
            #because we use sets
            self.vertices[v1].add(v2)
        else:
            # print("ERROR: vertex does not exist")
            raise ValueError("vertex does not exist")

def earliest_ancestor(ancestors, starting_node):
    #given the dataset and the ID of an individual in the dataset
        #returns their earliest known ancestor  
        #the one at the farthest distance from the input individual.
        #If there is more than one ancestor tied for "earliest"
            #return the one with the lowest numeric ID
            #If the input individual has no parents
                # the function should return -1
    graph = Graph()
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        #adds parent
        graph.add_vertex(parent)
        #adds child
        graph.add_vertex(child)
        #add edges from child to parent
        graph.add_edge(child, parent)
    
    #BFS
    queue = Queue()
    #path of starting node
    queue.enqueue( [starting_node ])

    # Farthest distance from the input individual.
    longest_path_length = 1
    # Has no parents, the function should return -1
    # If there is more than one ancestor tied for "earliest"
    earliest_ancestor = -1
    # While the queue is not empty
    while queue.size() > 0:
        # dequeue the first path
        # Since creating a path, order matters
        path = queue.dequeue()
        # returns -1 if there is no grandparent
        current_node = path[-1]

        #keeps track of longest path with the earliest ancestor or if the path length is greater than the longest path
        if len(path) >= longest_path_length and current_node < earliest_ancestor or len(path) > longest_path_length: 
            # if current_node < earliest_ancestor: #or len(path) > longest_path_length:
            longest_path_length = len(path)
            earliest_ancestor = current_node
        
        #keeps track of longest path with the earliest ancestor (4 places)
        # As well as edges cases of a different input (4 or 11)
        # if len(path) > longest_path_length:
        #     longest_path_length = len(path)
        #     earliest_ancestor = current_node

        #
        neighbors = graph.vertices[current_node]
        # push (add) path to all neighbors
        for ancestor in neighbors:
            # make a copy of the path
            path_copy = list(path)
            # add the copied path to the neighbor
            path_copy.append(ancestor)
            queue.enqueue(path_copy)
    
    print(path)
    print(earliest_ancestor)
    return earliest_ancestor
