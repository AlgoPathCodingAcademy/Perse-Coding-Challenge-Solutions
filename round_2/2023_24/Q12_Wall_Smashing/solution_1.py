maze = []
rows = int(input())
for row in range(rows):
  row_list = list(input())
  maze.append(row_list)

#print(maze)
directions = [(-1,0),(1,0),(0,-1),(0,1)]
import heapq
to_do_list = []
start = (0,0)
steps = {}
for row in range(len(maze)):
  for column in range(len(maze[0])):
    steps[(row,column)] = (float("inf"),float("inf"))
steps[start] = (0,0)
to_do_list.append(((0,0),start))

answer = 0
while True:
  if len(to_do_list) == 0:
    break

  weight,node = heapq.heappop(to_do_list)
  walls,step = weight
  current_row,current_column = node

  if node == (len(maze)-1,len(maze)-1):
    answer = step
    break
    
  for drow,dcolumn in directions:
    newRow = drow + current_row
    newColumn = dcolumn + current_column
    if (newRow >=0 and newRow < len(maze)) and \
      (newColumn >= 0 and newColumn < len(maze[0])):
      weight = int(maze[newRow][newColumn])

      if weight == 1 and maze[current_row][current_column] == "1":
          continue          # would break two walls in a row – illegal
      
      if weight == 1:
        new_walls = walls + 1
        new_steps = step
      else:
        new_walls = walls
        new_steps = step + 1

      # relaxation check
      current_wall,current_steps = steps[(newRow,newColumn)]
      if new_walls < current_wall:
        steps[(newRow,newColumn)] = (new_walls,new_steps)
        heapq.heappush(to_do_list,((new_walls,new_steps),(newRow,newColumn)))
      elif new_walls == current_wall and new_steps < current_steps:
        steps[(newRow,newColumn)] = (new_walls,new_steps)
        heapq.heappush(to_do_list,((new_walls,new_steps),(newRow,newColumn)))
      

walls, total_steps = steps[(rows-1, rows-1)]
print(total_steps)
