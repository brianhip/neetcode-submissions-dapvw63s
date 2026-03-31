class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search the partition
        if nums[0] < nums[-1]:
            return nums[0]

        partition = self.binarySearchPartition(nums)
        return nums[partition]
    
    def binarySearchPartition(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left // 2)
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return mid
            if mid < len(nums) - 2 and nums[mid + 1] < nums[mid]:
                return mid + 1
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return 0