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

  def find_open_neighbors(self, i, j):
    neighbors = []
    if i - 1 >= 0:
      top = self.maze[i-1][j]
      if top == "." or top == "*":
        neighbors.append([i-1, j])
    if j - 1 >= 0:
      left = self.maze[i][j-1]
      if left == "." or left == "*":
        neighbors.append([i, j-1])
    if i + 1 < len(self.maze):
      bottom = self.maze[i+1][j]
      if bottom == "." or bottom == "*":
        neighbors.append([i+1, j])
    if j + 1 < len(self.maze[i]):
      right = self.maze[i][j+1]
      if right == "." or right == "*":
        neighbors.append([i, j+1])
    return neighbors

  def reached_goal(self, i, j):
    if self.maze[i][j] == "*":
      return True
    else:
      return False