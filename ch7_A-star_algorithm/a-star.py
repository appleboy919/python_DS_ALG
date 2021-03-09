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

from helpers import get_path, offsets, is_legal_pos, read_maze
from priority_queue import PriorityQueue


def heuristic(a, b):
    """
    calculates the Manhattan distance between two pairs of grid coordinates
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(maze, start, goal):
    pq = PriorityQueue()
    pq.put(start, 0)  # since start point will be popped, 0 is fine for here
    preds = {start: None}
    g_values = {start: 0}
    while not pq.is_empty():
        current = pq.get()
        if current == goal:
            return get_path(preds, start, goal)
        for direction in offsets:
            row_offset, col_offset = offsets[direction]
            neighbor = (current[0] + row_offset, current[1] + col_offset)
            if is_legal_pos(maze, neighbor) and neighbor not in g_values:
                new_cost = g_values[current] + 1
                g_values[neighbor] = new_cost
                f_value = new_cost + heuristic(goal, neighbor)
                pq.put(neighbor, f_value)
                preds[neighbor] = current
    return None


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_bfs.txt")
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = a_star(maze, start_pos, goal_pos)
    assert result is None
