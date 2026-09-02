class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # find min use that as the first indext
        # 
        first_index = min(nums)
        total_nums = len(nums)
        # at most there can be a sequence of 1 to n
        for i in range(total_nums):
            if nums[i] <= 0:
                continue
            to_be_replaced = nums[i]
            out_of_bounds = to_be_replaced > total_nums
            # print("i", i, "to be replaced:", to_be_replaced, "out of bounds:", out_of_bounds, "nums", nums)
            j = total_nums
            while j > 0 and nums[i] - 1 != i and to_be_replaced > 0 and not out_of_bounds and (to_be_replaced != nums[to_be_replaced - 1]):
                # print("\tWHILE", j, "to be replaced:", to_be_replaced, "out of bounds:", out_of_bounds, "nums", nums)
                temp = to_be_replaced
                to_be_replaced = nums[to_be_replaced - 1]
                nums[temp - 1] = temp
                out_of_bounds = to_be_replaced > total_nums
                # print("\tWHILE", j, "to be replaced:", to_be_replaced, "out of bounds:", out_of_bounds, "nums", nums)
                # print()
                j -= 1
        # print(nums)
        for i in range(total_nums):
            if nums[i] != i + 1:
                return i + 1
        return total_nums + 1
