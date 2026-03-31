class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def builder(index, curr_lst, curr_sum):
            if index >= len(nums) or curr_sum > target:
                return
            if curr_sum == target:
                output.append(curr_lst.copy())
                return
            curr_lst.append(nums[index])
            builder(index, curr_lst, curr_sum + nums[index])
            curr_lst.pop()
            index += 1
            builder(index, curr_lst, curr_sum)
        builder(0, [], 0)
        return output