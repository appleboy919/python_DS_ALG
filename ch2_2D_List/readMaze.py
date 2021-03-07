# reads a text file which represents a maze

def read_maze(fileName):
    """
    Reads a maze stored in a text file and returns a 2d list containing the maze representation
    :param fileName: name of file
    :return: 2D list representing a maze
    """
    try:
        with open(fileName) as f:
            maze = [[char for char in line.strip('\n')] for line in f]
            num_cols = len(maze[0])
            for row in maze:
                if len(row) != num_cols:
                    print('The maze is not rectangular.')
                    raise SystemExit
            return maze
    except OSError:
        print('There is a problem with the file.')
        raise SystemExit


if __name__ == '__main__':

    maze = read_maze('mazes/modest_maze.txt')
    for row in maze:
        print(row)
