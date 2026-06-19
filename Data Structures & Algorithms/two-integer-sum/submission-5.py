class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Find the two numbers that equal the target sum
        # Return the indeces
        # Normally there's two approaches: 1. Sort and two pointers to wiggle them into the correct indeces 2. Iterate from left to right and calculate the diff from current number to target and see if you've visited before
        complements = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complements:
                return [complements[complement], i]
            complements[nums[i]] = i
        return [-1, -1]