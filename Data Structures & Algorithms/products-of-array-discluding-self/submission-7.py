class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Caluclate a global product of all items then for every index divide global over current index item
        # Allow for a single 0 that lead into having only a correct result of all items but itself
        total_product = 1
        seen_zero = False
        index_zero = -1
        output = [ 0 for i in range(len(nums))]
        for i, num in enumerate(nums):
            if num == 0:
                if seen_zero:
                    return output
                seen_zero = True
                index_zero = i
                continue
            else:
                total_product *= num
        if seen_zero:
            output[index_zero] = total_product
        else:
            for i, num in enumerate(nums):
                output[i] = total_product // num
        return output
