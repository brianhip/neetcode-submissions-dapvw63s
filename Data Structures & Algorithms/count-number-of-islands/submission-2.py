class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        def explore(i, j):
            in_range_and_land = 0 <= i < ROWS and 0 <= j < COLS and grid[i][j] == '1'
            if not in_range_and_land:
                return
            grid[i][j] = '0'
            for i_d, j_d in ((-1, 0), (1,0), (0,-1), (0,1)):
                explore(i + i_d, j + j_d)

        number_of_islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    number_of_islands += 1
                    explore(i, j)
        return number_of_islands
