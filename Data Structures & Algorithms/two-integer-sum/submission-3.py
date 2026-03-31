class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' 
            Understand: 
                Input: a list with numbers P
                Output: a list [] with the indeces of numbers that add up to the target
                Blackbox: Find a pair of numbers that sum to the target
            Match:
                1. Two pointer approach  RUN: O(n log n) SPACE: O(n) to store the original indeces
                2. Use a dictionary (HashMap) to store key: number value: index of value in the array
            Plan:
                2. Use a dictionary (HashMap) to store key: number value: index of value in the array
                    Initiate a dictionary
                    Iterate over the nums list
                        Calculate the complementary number necessary to add up to the target
                        Check if the complement number exists in the dictionary
                            Yes -> return the value  which is the index in the dictionary for the complementary number as well as the current index in a list
                            No -> add current as key and index as value to the dictionary 
        '''
        complements = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [complements[complement], i]
            else:
                complements[num] = i
        return [-1, -1]