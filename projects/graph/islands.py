# Write a function that takes a 2D binary array and 
# returns the number of 1 islands. 
# An island consists of 1s that are connected to the north, south, east or west. 
# For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

#islands consists of - conencted components (sub graph)
#connected (neighbors/edges)
#directions:n,e,s,w (edges too)
#2d array - is the graph more or less
#returns (shape of solution) - number of islands

# How could we write a get neighbor function that uses this shape?
# Offset coordinates

# How to find the extent of an island?
# Either of our travels to find all the nodes in an island

# How do I explore the larger set?
# Loop through and call a traversal is we find an unvisited

"""
Write a function that takes a 2D binary array
returns the number of 1 islands. 
island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4
"""
'''
Parallel arrays are islands and visited

Example visted matrix

visited = [[False, False, False, False, False],
          [False, False, False, False, False],
           [False, False, False, False, False],
           [False, False, False, False, False],
           [False, False, False, False, False]
'''
'''
for each node:
    if node not visited and the node is "land":
        traverse from that node #shows visited
        increment counter
'''

# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0]]

islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
#1. Translate the problem into graph terminology
#2. Build your graph
#3. Traverse your graph.
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def get_neighbors(row, col, matrix): #can only have 4 neighbors, want to know all 
    neighbors = []
   
    # Check North
    # if node at row, col (3,4)
    if row > 0 and matrix[row-1][col] == 1:
        neighbors.append((row-1, col))
    # Check south
    if row < len(matrix) -1 and matrix[row+1][col] == 1:
        neighbors.append((row+1, col))
    # check west
    if col > 0 and matrix[row][col-1] == 1:
        neighbors.append((row, col-1))
    # check east
    if col < len(matrix[0]) - 1 and matrix[row][col+1] == 1:
        neighbors.append((row, col+1))
    return neighbors


def dft(row, col, matrix, visited):
    s = Stack()

    s.push( (row, col) ) #tuple
    while s.size() > 0:
        row, col = s.pop()

        if not visited[row][col]:
            # visited[row][col] = True 
            # same as below
            visited_row = visited[row]
            visited_row[col] = True

            for neighbor in get_neighbors(row, col, matrix):
                s.push(neighbor)


# def island_counter(matrix): # 2D array (aka list of lists)
#     island_count = 0

#     # create visted martix
#     visited = []

#4 of them, 2D array,aka list of lists
def island_counter(matrix):
    island_count = 0
    #create a vistied matrix
    visited = []

    for _ in range(len(matrix)):
        #make a new row
        visited.append([False] * len(matrix[0])) # make list of falses if not visited
    # Walk though each cell in the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            #if not visited
            if not visited[row][col]:
                #if it's a "1"
                if matrix[row][col] == 1:
                    # DO DFt and mark visited
                    dft(row, col, matrix, visited)
                    #increment counter by 1
                    island_count += 1
    #return counter
    return island_count

print(island_counter(islands))  


# def island_counter(matrix): #2D array
#     # Create a visited matrix
#     visited = []
#     for i in range(len(matrix)):
#         visited.append([False] * len(matrix[0]))
#     island_count = 0
#     # for all nodes:
#     for col in range(len(matrix[0])):
#         for row in range(len(matrix)):
#             # if node is not visited:
#             if not visited[row][col]:
#                 # If we hit a 1 that has not been visited
#                 if matrix[row][col] == 1:
#                     # mark visited
#                     # traverse all connected nodes, marking as visited
#                     visited = dft(row, col, matrix, visited)
#                     # increment visited count
#                     island_count += 1
#     return island_count

# def dft(start_row, start_col, matrix, visited):
#     # Create a stack
#     s = Stack()
#     # Push the starting vertex
#     s.push((start_row, start_col))
#     # While the stack is not empty...
#     while s.size() > 0:
#         # Pop the first vertex
#         v = s.pop()
#         row = v[0]
#         col = v[1]
#         # Check if it's been visited
#         # If it hasn't been visited...
#         if not visited[row][col]:
#             # Mark it as visited
#             visited[row][col] = True
#             # Push all it's neighbors onto the stack
#             for neighbor in get_neighbors(row, col, matrix):
#                 s.push(neighbor)
#     # Return an updated visited matrix with all connected components marked as visited
#     return visited
    
    # def get_neighbors(row, col, matrix):
    # '''
    # Return a list of neighboring 1 tuples in the form [(row, col)]
    # '''
    # neighbors = []
    # # check north
    # if row > 0 and matrix[row-1][col] == 1:
    #     neighbors.append( (row-1, col) )
    # # check south
    # if row < len(matrix) - 1 and matrix[row+1][col] == 1:
    #     neighbors.append( (row+1, col) )
    # # check east
    # if col < len(matrix[0]) - 1 and matrix[row][col+1] == 1:
    #     neighbors.append( (row, col+1) )
    # # check west
    # if col > 0 and matrix[row][col-1] == 1:
    #     neighbors.append( (row, col-1) )
    # return neighbors
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0]]
# ​
# islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
#            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
#            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
#            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
#            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
#            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
#            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
#            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
#            [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
#            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
# ​
# print(island_counter(islands)) # returns 13