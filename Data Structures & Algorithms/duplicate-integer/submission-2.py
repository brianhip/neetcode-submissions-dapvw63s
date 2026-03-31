class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_duplicate_count = len(set(nums))
        total_list_count = len(nums)
        return non_duplicate_count != total_list_count
