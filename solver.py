class MazeSolver:

  def __init__(self, filename):
    self.maze = self.read_maze(filename)

  def read_maze(self, filename):
    file = open(filename, "r")
    lines = file.read().split("\n")
    maze = []
    for line in lines:
      line = list(line)
      maze.append(line)
    return maze

  def find_start(self):
    for i, line in enumerate(self.maze):
      for j, space in enumerate(line):
        if space == "o":
          return [i, j]

  def find_open_neighbors(self, i, j, previous):
    neighbors = []
    if i - 1 >= 0 and previous != [i-1, j]:
      top = self.maze[i-1][j]
      if top == "." or top == "*":
        neighbors.append([i-1, j])
    if j - 1 >= 0 and previous != [i, j-1]:
      left = self.maze[i][j-1]
      if left == "." or left == "*":
        neighbors.append([i, j-1])
    if i + 1 < len(self.maze) and previous != [i+1, j]:
      bottom = self.maze[i+1][j]
      if bottom == "." or bottom == "*":
        neighbors.append([i+1, j])
    if j + 1 < len(self.maze[i]) and previous != [i, j+1]:
      right = self.maze[i][j+1]
      if right == "." or right == "*":
        neighbors.append([i, j+1])
    return neighbors

  def reached_goal(self, i, j):
    if self.maze[i][j] == "*":
      return True
    else:
      return False

  def start_walk(self):
    start_space = self.find_start()
    return self.walk(start_space)

  def walk(self, current_space, previous=[]):
    if self.reached_goal(current_space[0], current_space[1]):
      return True
    neighbors = self.find_open_neighbors(current_space[0], current_space[1], previous)
    if neighbors == []:
      return False
    elif len(neighbors) == 3:
      return self.walk(neighbors[0], current_space) or self.walk(neighbors[1], current_space) or self.walk(neighbors[2], current_space)
    elif len(neighbors) == 2:
      return self.walk(neighbors[0], current_space) or self.walk(neighbors[1], current_space)
    else:
      return self.walk(neighbors[0], current_space)