class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            Understand: 
                Input: list with nums
                Output: length of the longest consecutive sequence of elements that can be formed
                Blackbox: This will find the longest consecutive secuence of numbers
                Constaints: nums.length 0 - 1000 
                Obsevations: 
                    The longest consecutive sequence does not have to be in a specific order
            Match:
                Brute force:
                    calcualte all possible sequences that end at specifc index O(n^2)
                DP:
                    Use an array of same size as nums to store the longes sequence at this location
                    Calculate the longest sequence by  using the 
            Plan:
            Implement:
            Review:
            Evaluate:
        '''
        # get unique numbers
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # To be optimal only count the first number in a consecutive sequence (s1, s2, ... , sn-1, sn) only count when you find s1. s1 should not have a number prior otherwise that number would be the starting of the sequence.
            prev_num = num - 1
            if prev_num not in num_set:
                length = 1
                next_num = num + 1
                while next_num in num_set:
                    next_num += 1
                longest = max(next_num - num, longest)

        return longest
        