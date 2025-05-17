num_rows = int(input())
maze = []
for _ in range(num_rows):
    row = input().strip()
    maze.append(row)

start = (0, 0)

# ------------------------------------------------------------------
# distance[(r,c)] -> (walls_broken, steps_taken)
# ------------------------------------------------------------------
distance = {(i, j): (float("inf"), float("inf"))
            for i in range(num_rows) for j in range(num_rows)}
distance[start] = (0, 0)                       # store a tuple

import heapq

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
to_do_list = []
heapq.heappush(to_do_list, (0, 0, 0, 0))       # (walls, steps, row, col)

while to_do_list:
    walls, steps, row, column = heapq.heappop(to_do_list)

    if (row, column) == (num_rows - 1, num_rows - 1):
        break

    for drow, dcolumn in directions:
        new_row = row + drow
        new_column = column + dcolumn
        if 0 <= new_row < num_rows and 0 <= new_column < num_rows:

            # -------------------------------------------------------
            # Case A — neighbour is corridor (0)
            # -------------------------------------------------------
            if maze[new_row][new_column] == '0':
                if (walls, steps + 1) < distance[(new_row, new_column)]:
                    distance[(new_row, new_column)] = (walls, steps + 1)
                    heapq.heappush(to_do_list,
                                   (walls, steps + 1, new_row, new_column))

            # -------------------------------------------------------
            # Case B — neighbour is wall (1): try to hop over it
            # -------------------------------------------------------
            else:
                hop_row = new_row + drow
                hop_col = new_column + dcolumn
                if (0 <= hop_row < num_rows and 0 <= hop_col < num_rows
                        and maze[hop_row][hop_col] == '0'):

                    if (walls + 1, steps + 1) < distance[(hop_row, hop_col)]:
                        distance[(hop_row, hop_col)] = (walls + 1, steps + 1)
                        heapq.heappush(to_do_list,
                                       (walls + 1, steps + 1, hop_row, hop_col))

# ------------------------------------------------------------------
# answer: second element of the tuple (steps)
# ------------------------------------------------------------------
print(distance[(num_rows - 1, num_rows - 1)][1])
