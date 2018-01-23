import solver

maze = solver.read_maze("maze.txt")

def test_read_maze():
  assert maze == [['o','.','#'],['#','.','*'],['#','#','#']]

def test_find_start():
  assert solver.find_start(maze) == [0,0]