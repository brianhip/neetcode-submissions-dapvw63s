class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            Understad:
                Input: 2-D list with ones representing land and zeros representing water
                Ouput: count the number of islands based on the number of ones surrounded by 0s or nothing in the top, bottom, left, right directions
            Match:
                Dfs convert every land into a "#" until land has no more neighboring land
                for every one in the matrix call the dfs converter and increase the count of island
            Plan:
                have a helper function that will explore in 4 direction to see if we have neighboring land
                if x or y are not in bounds or current index is water or current index is hastag return
                conver current land into "#"
                convert all four directions
                return

                have a for loop that iterates every row from top to bottom and for every row it iterate every number  from left to right
                    for every number that is a one call the converter and increase the numebr of islands
            Implement:
            Review:
            Evaluate:
        '''
        height = len(grid)
        width  = len(grid[0])
        def island_explorer_dfs(y: int, x: int) -> None:
            out_of_bounds = (y < 0 or height <= y or x < 0 or width <= x)
            if out_of_bounds or grid[y][x] != "1":
                return
            grid[y][x] = "#"
            island_explorer_dfs(y - 1, x)
            island_explorer_dfs(y + 1, x)
            island_explorer_dfs(y, x - 1)
            island_explorer_dfs(y, x + 1)
            return
        islands_count = 0
        for y, row in enumerate(grid):
            for x, char in enumerate(row):
                if char == "1":
                    island_explorer_dfs(y, x)
                    islands_count += 1
        return islands_count