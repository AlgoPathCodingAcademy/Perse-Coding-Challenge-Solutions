target_row = int(input()) - 1
target_column = int(input()) - 1

maze = []
for i in range(10):
  maze.append([int(item) for item in input()])

total_column = 0
for row in range(10):
    for column in range(10):
      if column == target_column:
        total_column = total_column + maze[row][column]

total_row = sum(maze[target_row])

print(total_row+total_column-maze[target_row][target_column])
