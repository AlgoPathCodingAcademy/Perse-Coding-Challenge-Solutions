rows = int(input())
columns = rows
src = int(input())
dest = int(input())
maze = []

for i in range(rows):
  row = []
  for j in range(columns):
    row.append(0)
  maze.append(row)

#Show Empty Maze
#print(maze)

start = (0,0)
from collections import deque
visited = {}
visited[start] = True
to_do_list = deque()
to_do_list.append(start)

directions = [(-1,0),(0,-1),(1,0),(0,1)]

counter = 1

location_hash = {}

while True:
  if len(to_do_list) == 0:
    break
    
  row,column = to_do_list.popleft()

  maze[row][column] = counter
  location_hash[counter] = (row,column)

  counter = counter + 1

  for drow,dcolumn in directions:
    new_row = row + drow
    new_column = column + dcolumn

    if (new_row >=0 and new_row < rows) and \
      (new_column >= 0 and new_column < columns):
      if (new_row,new_column) not in visited:
        visited[(new_row,new_column)] = True
        to_do_list.append((new_row,new_column))

#Show Maze After BFS
#print(maze)

maze_start = location_hash[src]
maze_end = location_hash[dest]
steps = {}
steps[maze_start] = 0

maze_visited = {}
maze_visited[maze_start] = True

maze_to_do_list = deque()
maze_to_do_list.append(maze_start)

maze_directions = [(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0)]

while True:
  if len(maze_to_do_list) == 0:
    break

  row, column = maze_to_do_list.popleft()

  if (row,column) == maze_end:
    break
  
  for drow,dcolumn in maze_directions:
    new_row = row + drow
    new_column = column + dcolumn

    if (new_row >=0 and new_row < rows) and \
      (new_column >= 0 and new_column < columns):
      if (new_row,new_column) not in maze_visited:
        maze_visited[(new_row,new_column)] = True
        maze_to_do_list.append((new_row,new_column))
        steps[(new_row,new_column)] = steps[(row,column)] + 1

print(steps[maze_end]+1)
