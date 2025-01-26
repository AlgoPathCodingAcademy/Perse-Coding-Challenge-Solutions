rows = int(input())
columns = rows
pattern = input()

first_line = ""
for i in range(rows):
  first_line = first_line + pattern[i%len(pattern)]

print(first_line)

index = rows%len(pattern)
for j in range(rows-1):
  for i in range(columns):
    if i == rows//2:
      print(pattern[index%len(pattern)],end="")
      index = index + 1
    else:
      print(".",end="")
  print("")
