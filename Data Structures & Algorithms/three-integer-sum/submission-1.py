class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # For every number find if there is a two sum that adds up to current number
        nums.sort()
        added = set()
        output = []
        for first_i in range(len(nums) - 2):
            subset_list = self.twoSum(nums, first_i + 1, -nums[first_i])
            for subset in subset_list:
                key = f"{subset[0]},{subset[1]},{subset[2]}"
                if key not in added:
                    output.append(subset)
                    added.add(key)
        return output
    def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        output = []
        seen = set()
        for i in range(start, len(nums)):
            complement = target - nums[i]
            if complement in seen:
                output.append([-target, complement, nums[i]])
            else:
                seen.add(nums[i])
        return output
