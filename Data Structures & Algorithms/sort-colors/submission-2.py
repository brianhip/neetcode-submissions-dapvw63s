class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_white_blue = [0, 0, 0]
        for color in nums:
            red_white_blue[color] += 1

        for i in range(len(nums)):
            if i < red_white_blue[0]:
                nums[i] = 0
            elif i < red_white_blue[0] + red_white_blue[1]:
                nums[i] = 1
            else:
                nums[i] = 2
        return nums