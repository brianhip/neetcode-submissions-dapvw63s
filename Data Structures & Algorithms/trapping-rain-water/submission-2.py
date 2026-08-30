class Solution:
    def trap(self, height: List[int]) -> int:
        WIDTH = len(height)

        left_walls = [0 for i in range(WIDTH)]
        right_walls = [0 for i in range(WIDTH)]

        for i in range(WIDTH):
            if i==0:
                left_walls[i] = height[i]
                continue
            left_walls[i] = max(height[i], left_walls[i-1])
        
        for i in range(WIDTH-1, -1, -1):
            if i==WIDTH-1:
                right_walls[i] = height[i]
                continue
            right_walls[i] = max(height[i], right_walls[i+1])
        
        current_rain = 0
        for i in range(WIDTH):
            shortest = min(left_walls[i], right_walls[i])
            current_rain += shortest - height[i]
        return current_rain