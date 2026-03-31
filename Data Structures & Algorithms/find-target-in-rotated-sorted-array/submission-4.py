class Solution:
    def search(self, nums: List[int], target: int) -> int:
        partition = self.findPartition(nums)
        target_is_to_the_right = nums[partition] <= target and target <= nums[len(nums) - 1]
        left, right = (partition, len(nums) - 1) if target_is_to_the_right else (0, partition)
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def findPartition(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return mid
            # if mid < len(nums) - 2 and nums[mid + 1] < nums[mid]:
            #     return mid + 1
            
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return 0
                