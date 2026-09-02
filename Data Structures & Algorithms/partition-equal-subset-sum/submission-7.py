class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        max_num = max(nums)
        target = total_sum // 2 
        if total_sum % 2 == 1 or target < max_num:
            return False
        N = len(nums)
        nums.sort()
        dp = [[ False for _ in range(target + 1)] for i in range(N + 1)]
        for i in range(N + 1):
            dp[i][0] = False
        for b in range(target + 1):
            dp[0][b] = False
        
        for i in range(1, N + 1):
            for j in range(1, target + 1):
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]  
                else:
                    if nums[i - 1] == j or dp[i - 1][j - nums[i - 1]]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
        return dp[N][target]