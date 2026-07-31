class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            Take or leave
                if only can take one item then move
                if more than one item take stays and leave moves
            output = []
            def combinations (index, curr_sum, curr_combination, output)
                base cases:
                    1. current sum equals target then append the curr_combination to output and return 
                    2. index is out of bounds then return
                    3. current sum is greater than target then return too
                
                recursive case:
                    1. take: append current number to the curr_combination, pass as curr_sum: curr_sum + current number and pass same index
                    2. leave: remove previously added number to the curr_combination and move index forward                    
        """
        testing = []
        def combinations(index, curr_sum, curr_combination):
            if curr_sum == target:
                testing.append(curr_combination.copy())
                return
            if index >= len(nums) or curr_sum > target:
                return 
            
            curr_combination.append(nums[index])
            combinations(index, curr_sum + nums[index], curr_combination)
            curr_combination.pop()
            combinations(index + 1, curr_sum, curr_combination)
        
        combinations(0, 0, [])

        return testing