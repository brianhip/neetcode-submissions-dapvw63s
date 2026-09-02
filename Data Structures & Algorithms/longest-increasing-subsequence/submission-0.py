class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        total_numbers = len(nums)
        dp = [ 1 for _ in range(total_numbers)]
        for i in range(1, total_numbers):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1 
        return max(dp)