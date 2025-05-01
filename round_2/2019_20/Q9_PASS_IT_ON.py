nums = int(input())
start_flag = False
start = ""
adj_list = {}
for _ in range(nums):
  line = input().split(":")
  u = line[0]
  if not start_flag:
    start = u
    start_flag = True
  v_list = list(line[1])
  adj_list[u] = v_list

path = {}
path[start] = 0

from collections import deque
to_do_list = deque([start])
visited = {}
visited[start] = True

while True:
  if len(to_do_list) == 0:
    break

  current = to_do_list.popleft()

  for neighbor in adj_list[current]:
    if neighbor not in visited:
      visited[neighbor] = True
      to_do_list.append(neighbor)
      path[neighbor] = path[current] + 1

max_length = max(path.values())
print(max_length)
