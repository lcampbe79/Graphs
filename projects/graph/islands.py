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