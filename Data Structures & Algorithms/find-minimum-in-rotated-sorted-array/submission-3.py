class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1 2 3 4 5 
        # 5 1 2 3 4
        # 4 5 1 2 3
        # 3 4 5 1 2
        # 2 3 4 5 1

        # IDEAS/Observations:
        # Base case: if the first number in the nums list is less than last num then return that num
        # If we want the min number in log n time we need to use Binary Search
        # To find the min number using binary search we are searching for a case where num_i > num_i+1 
        # To cut the searching space in half we would like to make sure that partition is in the half we're keeping
            # The partition is on the side where a normal ascending order is not represented (NORMAL: start<mid<end NOT-NORMAL: start>mid OR mid>end)

        # while the searching space is valid (>0)
            # check the middle to see if previous number is greater YES: return nums[mid] NO: continue next
            # cut the searching space in half by checking 
            # IF nums[mid]<nums[start] -> make end pointer = mid - 1 ELSE start = mid + 1

        start = 0
        end = len(nums) - 1

        if nums[start] <= nums[end]:
            return nums[start]

        while start <= end:
            mid = start + (end - start) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
        
            if nums[start] > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return nums[0]

