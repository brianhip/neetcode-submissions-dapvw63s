class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two pointer and wiggle inwar the shortes pointer until they meet each other: 
        #   keep track of the max_area = max(max_area, curr_area)
        #   curr_area = (right - left) * min(height_left, height_right)
        max_area = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            min_height = min(heights[left], heights[right])
            current_area = (right - left) * min_height
            max_area = max(max_area, current_area)
            if min_height == heights[left]:
                left += 1
            else:
                right -= 1
        return max_area
