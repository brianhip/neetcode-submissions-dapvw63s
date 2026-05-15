class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge(nums)

    def merge(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.merge(nums[:mid])
        right = self.merge(nums[mid:])
        output = []
        l_len = len(left)
        r_len = len(right)
        i = 0
        j = 0
        while i < l_len and j < r_len: 
            if left[i] <= right[j]:
                output.append(left[i])
                i += 1
            else:
                output.append(right[j])
                j += 1
        while i < l_len : 
            output.append(left[i])
            i += 1
        while j < r_len:
            output.append(right[j])
            j += 1
        return output
