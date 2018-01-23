def read_maze(filename):
  file = open(filename, "r")
  lines = file.read().split("\n")
  maze = []
  for line in lines:
    line = list(line)
    maze.append(line)
  return maze

def find_start(maze):
  for i, line in enumerate(maze):
    for j, space in enumerate(line):
      if space == "o":
        return [i, j]