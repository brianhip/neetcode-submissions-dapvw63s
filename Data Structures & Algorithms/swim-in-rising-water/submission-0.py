import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # path with the shortest height
        HEIGHT = len(grid)
        WIDTH = len(grid[0])
        seen = set()
        max_path_height = 0
        queue = [(grid[0][0], (0,0))]
        while queue:
            curr_height, coordinates = heapq.heappop(queue)
            if coordinates in seen:
                continue
            seen.add(coordinates)
            max_path_height = max(max_path_height, curr_height)
            if coordinates == (HEIGHT - 1, WIDTH - 1):
                break
            x, y = coordinates
            for x_d, y_d in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_x, new_y = x + x_d, y + y_d
                in_range = 0 <= new_x < HEIGHT and 0 <= new_y < WIDTH
                if not in_range:
                    continue
                heapq.heappush(queue, [grid[new_x][new_y], (new_x, new_y)])
        return max_path_height