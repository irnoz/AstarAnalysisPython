import Maze
from BinomialHeap import BinomialHeap

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
    def __hash__(self):
        return hash(self.position)
    
    def __lt__(self, other):
        return self.f < other.f

def astar(maze, start, end):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = BinomialHeap()
    closed_set = set()

    open_list.insert(start_node)
    
    while open_list:
        current_node = open_list.extract_min()
        closed_set.add(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > len(maze) - 1 or node_position[0] < 0 or \
               node_position[1] > len(maze[len(maze)-1]) - 1 or node_position[1] < 0:
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            if child in closed_set:
                continue

            child.g = current_node.g + 1
            child.h = (child.position[0] - end_node.position[0]) ** 2 + (child.position[1] - end_node.position[1]) ** 2
            child.f = child.g + child.h

            if (child.f, child) in open_list:
                continue

            open_list.insert(child)

def main():
    path = astar(Maze.maze, Maze.start, Maze.end)
    print(path)

if __name__ == '__main__':
    main()
