class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            Understand:
                Input:
                    array with number
                Ouput:
                    array created form the product of all numbers except itself from the original array
                Blackbox:
                    Give an array of size n with n numbers
                    Returns an array of size n with the product of all other numbers than that index
                Constraint:
                    No use of the divide operator
                Observations:
                    If ONE zeroe in array then the only non-zero product will be at that index
                    If MORE than ONE zero in array then entire output array should be 0
                
            Match:
                Build the left product then the right product then when building the final output array use the left and right product
            Plan:
                Create an array with product of numbers left to current number
                Create an array with product of numbers right to the current numebr
                Zip and iterate through the arrays
                    multiply each indeces against each other
                output final array
            Implement:
            Review:
            Evaluate:
        '''
        left_products = []
        curr_product = 1
        for i in range(len(nums)):
            left_products.append(curr_product)
            curr_product *= nums[i]

        curr_product = 1
        for i in range(len(nums) - 1, -1, -1):
            left_products[i] *= curr_product
            curr_product *= nums[i]

        return left_products