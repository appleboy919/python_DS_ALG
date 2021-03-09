# application: GPS systems, flight reservation system, SNS to find connection
# btw users, Web crawlers, AI, scientific modeling

# implementation of BFS algorithm using Queue

from helpers import get_path, offsets, is_legal_pos, read_maze
from myQueue import Queue

def bfs(maze, start, goal):
    queue = Queue()
    queue.enqueue(start)
    preds = {start: None}
    while not queue.is_empty():
        current = queue.dequeue()
        if current == goal:
            return get_path(preds, start, goal)
        for direction in offsets:
            row_offset, col_offset = offsets[direction]
            neighbor = (current[0] + row_offset, current[1] + col_offset)
            if is_legal_pos(maze, neighbor) and neighbor not in preds:
                queue.enqueue(neighbor)
                preds[neighbor] = current
    return None


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
    print('Test 1 passed....!')

    # Test 2
    maze = read_maze("mazes/mini_maze_bfs.txt")
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]
    print('Test 2 passed....!')


    # Test 3
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    assert result is None
    print('Test 3 passed....!')

