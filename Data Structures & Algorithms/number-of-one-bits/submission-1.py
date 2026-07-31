class Solution:
    def hammingWeight(self, n: int) -> int:
        # to convert a number to bits you can divide and by two 
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res