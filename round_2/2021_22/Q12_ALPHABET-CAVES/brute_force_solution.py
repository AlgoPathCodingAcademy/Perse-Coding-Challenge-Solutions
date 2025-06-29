letters = input()
index = int(input()) - 1

visited = {}

result = []

path = letters[0]

def dfs(path,result,visited):
  current = path[-1]

  if current == letters[-1]:
    result.append(path)

  current_index = letters.index(current)

  left = None
  right = None
  if current_index+1 < len(letters):
    left = letters[current_index+1]

  if current_index+2 < len(letters):
    right = letters[current_index+2]

  if current not in visited:
    visited[current] = True
    if left != None:
      dfs(path+left,result,visited)
    if right != None:
      dfs(path+right,result,visited)
    del visited[current]

dfs(path,result,visited)

print(result[index])
