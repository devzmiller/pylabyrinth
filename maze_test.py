from solver import MazeSolver

mazesolver = MazeSolver("maze.txt")

def test_read_maze():
  assert mazesolver.maze == [['o','.','#'],['#','.','*'],['#','#','#']]

def test_find_start():
  assert mazesolver.find_start() == [0,0]

def test_find_open_neighbors():
  assert mazesolver.find_open_neighbors(1, 1) == [[0,1],[1,2]]

def test_reached_goal():
  assert mazesolver.reached_goal(1,2) == True