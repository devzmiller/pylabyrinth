from solver import MazeSolver

mazesolver = MazeSolver("maze.txt")
mazesolver2 = MazeSolver("map2.txt")

def test_read_maze():
  assert mazesolver.maze == [['o','.','#'],['#','.','*'],['#','#','#']]

def test_find_start():
  assert mazesolver.find_start() == [0,0]

def test_find_open_neighbors():
  assert mazesolver.find_open_neighbors(1, 1, []) == [[0,1],[1,2]]
  assert mazesolver.find_open_neighbors(2, 0, []) == []

def test_reached_goal():
  assert mazesolver.reached_goal(1,2) == True

def test_start_walk_solvable():
  assert mazesolver.start_walk() == True

def test_start_walk_unsolvable():
  assert mazesolver2.start_walk() == False