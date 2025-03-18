# Further optimization could be done to replace the integer to string
# to avoid arithmetic operation when the numnber becomes large.

from collections import deque
number = int(input())
start = (1,1)
visited = {}
visited[1] = True

to_do_list = deque()
to_do_list.append(start)

answer = float("inf")

def getNeighbors(current,n):
  result = []
  result.append(((current*10)%n,current*10))
  result.append(((current*10+1)%n,current*10+1))
  return result

while True:
  if len(to_do_list) == 0:
    break

  remainder,full_number = to_do_list.popleft()

  if full_number > 0 and remainder == 0:
    answer = full_number
    break

  neighbors = getNeighbors(full_number,number)

  for neighbor_remainder, neighbor_full in neighbors:
    if neighbor_remainder not in visited:
      visited[neighbor_remainder] = True
      to_do_list.append((neighbor_remainder,neighbor_full))

print(answer)
