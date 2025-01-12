columns = int(input())
rows = int(input())

max_number = float("-inf")
maze = []

for _ in range(rows):
  row = [int(item) for item in input().split(" ")]
  maze.append(row)

result_list = []

# Diagonal direction
compare_directions = [[1,1],[1,-1],[-1,1],[-1,-1]]

for row in range(len(maze)):
  for column in range(len(maze[0])):
    max_adj = float("-inf")
    for dx,dy in compare_directions:
      new_column,new_row = column + dy,row + dx
      if (new_column >= 0 and new_column < columns) and \
            (new_row >= 0 and new_row < rows):
        if maze[new_row][new_column] > max_adj:
          max_adj = maze[new_row][new_column]
    
    if max_adj*maze[row][column] > max_number:
      max_number = max_adj*maze[row][column]

print(max_number)
