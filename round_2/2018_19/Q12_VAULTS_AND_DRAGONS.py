# 0/1 BFS

# One special case occurs if the start point itself contains a dragon (“D”).
# To handle this, you can introduce a dummy node and link it to node 1 with a single one-way edge from the dummy node to node 1,
# similar to how dummy nodes are sometimes used in linked list implementations.

nums_dungeon = int(input())
condition = input()
nums_tunnels = int(input())
adj_list = {}

dest = 0
cost_list = {}

cost_list[0] = (0,0)
for i in range(len(condition)):
  if condition[i] == "E":
    cost_list[i+1] = (i+1,0)
  elif condition[i] == "D":
    cost_list[i+1] = (i+1,1)
  else:
    dest = i+1
    cost_list[i+1] = (i+1,0)


adj_list[0] = [cost_list[1]]
for _ in range(nums_tunnels):
  connection = [int(item) for item in input().split()]

  src_ = connection[0]
  dest_ = connection[1]


  if connection[0] not in adj_list:
    adj_list[connection[0]] = [cost_list[dest_]]
  else:
    adj_list[connection[0]].append(cost_list[dest_])

  if connection[1] not in adj_list:
    adj_list[connection[1]] = [cost_list[src_]]
  else:
    adj_list[connection[1]].append(cost_list[src_])


def run_bfs(start,dest,adj_list,nums_dungeon):
  from collections import deque
  to_do_list = deque()
  to_do_list.append(start)
  path = {}
  for i in range(1,nums_dungeon+1):
    path[i] = float("inf")

  path[start] = 0

  while True:
    if len(to_do_list) == 0:
      break

    node = to_do_list.popleft()
    
    for neighbor, cost in adj_list[node]:
      if path[node] + cost < path[neighbor]:
        path[neighbor] = path[node] + cost
        if cost == 0:
          to_do_list.appendleft(neighbor)
        else:
          to_do_list.append(neighbor)

  return path[dest]

steps = run_bfs(0,dest,adj_list,nums_dungeon)

print(steps)
