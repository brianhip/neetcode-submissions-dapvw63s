class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # longest consecutive subsequence
        # this could be a the sequence of number that are increasing
        set_nums = set(nums)
        max_consecutive = 0
        for i in range(len(nums)):
            num = nums[i]
            if num - 1 not in set_nums: # enter only on the smallest number of the sequences
                consecutive = 1
                while num + consecutive in set_nums:
                    consecutive += 1
                max_consecutive = max(max_consecutive, consecutive)
        return max_consecutive

        