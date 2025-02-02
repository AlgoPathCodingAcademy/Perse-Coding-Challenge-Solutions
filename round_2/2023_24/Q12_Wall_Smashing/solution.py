import heapq

def solve():
    n = int(input().strip())
    grid = []
    for _ in range(n):
        row_str = input().strip()
        row = [int(ch) for ch in row_str]
        grid.append(row)

    # cost[r][c] = (walls_broken, steps) best known to get to (r, c)
    INF = (10**9, 10**9)  # A large "infinite" tuple
    cost = [[INF]*n for _ in range(n)]
    cost[0][0] = (0, 0)  # start at top-left with 0 walls broken, 0 steps

    # Min-heap storing tuples: (walls_broken, steps, row, col)
    pq = [(0, 0, 0, 0)]

    # Directions for movement: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        walls, steps, r, c = heapq.heappop(pq)

        # If this is not our best known cost, skip
        if (walls, steps) != cost[r][c]:
            continue

        # If we've reached the destination, we're done
        if (r, c) == (n-1, n-1):
            print(steps)
            return

        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # 1) Normal move if next cell is free
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                new_cost = (walls, steps + 1)
                if new_cost < cost[nr][nc]:
                    cost[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost[0], new_cost[1], nr, nc))

            # 2) Wall-break move if next cell is a wall, *but* you only hop over it
            #    if the cell beyond is within bounds and is free.
            elif 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                br, bc = nr + dr, nc + dc  # the cell beyond the wall
                # Check that it's in bounds and free (cell == 0)
                if 0 <= br < n and 0 <= bc < n and grid[br][bc] == 0:
                    new_cost = (walls + 1, steps + 1)
                    if new_cost < cost[br][bc]:
                        cost[br][bc] = new_cost
                        heapq.heappush(pq, (new_cost[0], new_cost[1], br, bc))

    # If we exhaust the heap without reaching (n-1, n-1), no path exists
    print(-1)
solve()
