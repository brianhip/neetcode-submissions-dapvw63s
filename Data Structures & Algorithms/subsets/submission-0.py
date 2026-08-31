class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def generate_subset(i, curr):
            if i == len(nums):
                output.append(curr.copy())
                return
            curr.append(nums[i])
            generate_subset(i + 1, curr)
            curr.pop()
            generate_subset(i + 1, curr)
        generate_subset(0, [])
        return output
