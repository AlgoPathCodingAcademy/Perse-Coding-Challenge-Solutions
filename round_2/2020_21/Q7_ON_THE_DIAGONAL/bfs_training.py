columns = int(input())
rows = int(input())

maze = []

for _ in range(rows):
  row = [int(item) for item in input().split(" ")]
  maze.append(row)

#print(maze)

# BFS
# Use HashTable; If HashTable is not taught, use list instead.
visited = {}
visited[(0,0)] = True

to_do_list = [(0,0)]

# Use for BFS in four directions
directions = [[0,1],[0,-1],[1,0],[-1,0]]

# Use for adjacent diagonal check
compare_directions = [[1,1],[1,-1],[-1,1],[-1,-1]]

max_number = float("-inf")
while True:
  if len(to_do_list) == 0:
      break

  row_,column_ = to_do_list.pop(0)

  max_adj = float("-inf")
  adj_list = []
  for dx, dy in directions:
    new_column,new_row = column_ + dy,row_ + dx
    if (new_row,new_column) not in visited:
      if (new_column >= 0 and new_column < columns) and \
        (new_row >= 0 and new_row < rows):
        to_do_list.append((new_row,new_column))
        visited[(new_row,new_column)] = True

  # Check examine the adjacent diagonal positions
  for dx,dy in compare_directions:
    new_column,new_row = column_ + dy,row_ + dx
    if (new_column >= 0 and new_column < columns) and \
          (new_row >= 0 and new_row < rows):
      if maze[new_row][new_column] > max_adj:
        max_adj = maze[new_row][new_column]

  if max_adj*maze[row_][column_] > max_number:
    max_number = max_adj*maze[row_][column_]

print(max_number)
