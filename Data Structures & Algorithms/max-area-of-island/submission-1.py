class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        def explore(i, j):
            in_range = 0 <= i < ROWS and 0 <= j < COLS
            key = f"{i},{j}"
            if not in_range or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            current_area = 1
            for i_d, j_d in [(-1,0), (1,0), (0,-1), (0,1)]:
                current_area += explore(i + i_d, j + j_d)
            return current_area     
        
        max_area_island = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    max_area_island = max(
                        explore(i, j),
                        max_area_island
                    )
        return max_area_island
                    
        