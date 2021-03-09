# widely known algorithm for shortest path

# application: traffic naviagtional system, social network analysis, Natural
# language processing, Machine learning, puzzle solutions, algorithmic
# trading, robotics, video games

# ** USE OF HEURISTIC (a.k.a. rule of thumb) to determine the likely BEST
# CHOICE for each step of the algorithm
#       ==> heuristic: choose the next position to visit based on its
#       distance from the goal ('Manhattan distance' or 'Euclidean distance')

# Key values in A* algorithm
#   G value: best distance from start to current cell
#   H value: heuristic distance from current to destination
#   F value: sum of G, H values (representing the probable optimal value of
#   MIN distance based on heuristic used)



def a_star(maze, start, end):
