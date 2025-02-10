numsNodes = int(input())
lines = int(input())
adj_list = {}
for _ in range(lines):
  input_ = [int(item) for item in input().split()]
  src = input_[0]
  dest = input_[1]
  if src not in adj_list:
    adj_list[src] = [dest]
  else:
    adj_list[src].append(dest)

  if dest not in adj_list:
    adj_list[dest] = [src]
  else:
    adj_list[dest].append(src)

#print(adj_list)

# check single node 
for node in range(1,numsNodes+1):
  if node not in adj_list:
    adj_list[node] = []

visited = {}

def runBFS(node,adj_list,visited):
  visited[node] = True
  to_do_list = [node]
  traversal_list = []
  
  while True:
    if len(to_do_list) == 0:
      break

    current = to_do_list.pop(0)
    traversal_list.append(current)
    #print("visiting",current)

    for neighbor in adj_list[current]:
      if neighbor not in visited:
        to_do_list.append(neighbor)
        visited[neighbor] = True

  return traversal_list
  

resut_list = []
nums = 0
max_length = float("-inf")
for node in range(1,numsNodes+1):
  if node not in visited:
    chain_list = runBFS(node,adj_list,visited)
    #print("output chain_list",chain_list)
    nums = nums +1
    resut_list.append(chain_list)
    if len(chain_list) > max_length:
      max_length = len(chain_list)

print(max_length)
