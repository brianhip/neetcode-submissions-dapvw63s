class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        first_index = min(nums)
        total_nums = len(nums)
        for i in range(total_nums):
            if nums[i] <= 0:
                continue
            to_be_replaced = nums[i]
            out_of_bounds = to_be_replaced > total_nums
            j = total_nums
            while j > 0 and nums[i] - 1 != i and to_be_replaced > 0 and not out_of_bounds and (to_be_replaced != nums[to_be_replaced - 1]):
                temp = to_be_replaced
                to_be_replaced = nums[to_be_replaced - 1]
                nums[temp - 1] = temp
                out_of_bounds = to_be_replaced > total_nums
                
                j -= 1
        for i in range(total_nums):
            if nums[i] != i + 1:
                return i + 1
        return total_nums + 1
