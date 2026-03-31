class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        // Cache the numbers and indeces
        const mapa = new Map();
        // Iterate through the array and find the complementary required number to reach target
        for(let i = 0; i < nums.length; i++){
            let num = nums[i];
            let complement = target - num;
            if (mapa.has(complement)){
                return [mapa.get(complement), i];
            }
            mapa.set(num, i);
        }
        // Return indeces of numbers that add up to the correct number

    }
}
