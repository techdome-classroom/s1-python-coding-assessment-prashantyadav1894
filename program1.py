class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
  def numIslands(grid):
    if not grid:
        return 0

    def dfs(i, j):
        # Boundary check and whether the current cell is land ('L')
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
            return
        # Mark the current land as visited (turn it into water 'W')
        grid[i][j] = 'W'
        
        # Recursively explore adjacent cells (up, down, left, right)
        dfs(i + 1, j)  # Down
        dfs(i - 1, j)  # Up
        dfs(i, j + 1)  # Right
        dfs(i, j - 1)  # Left

    island_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'L':
                island_count += 1
                dfs(i, j)
                
    return island_count

# Test cases:

grid1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"]
]

grid2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"]
]

print(numIslands(grid1))  # Output: 1
print(numIslands(grid2))  # Output: 3

