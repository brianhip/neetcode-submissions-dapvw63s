class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # how many zeroes or out of bounds does the island have surrouning it
        def in_bounds(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        def dfs(i, j):
            if not in_bounds(i, j) or grid[i][j] in [0, -1]:
                return 0
            curr_perimeter = 0
            for i_d, j_d in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_i, new_j = i + i_d, j + j_d
                if not in_bounds(new_i, new_j) or grid[new_i][new_j] == 0:
                    curr_perimeter += 1
    
            grid[i][j] = -1
            for i_d, j_d in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_i, new_j = i + i_d, j + j_d
                curr_perimeter += dfs(new_i, new_j)
            return curr_perimeter
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0
            