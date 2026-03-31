class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    // The simplest form to solve it 
    // Find the product of nums and return an array of each num dividing the product to get the product of all except current
    // productExceptSelf(nums) {
    //     const numberZeroes = nums.reduce((prev, curr) => curr==0?prev+1:prev, 0);
    //     if (numberZeroes > 1) return Array(nums.length).fill(0);
    //     const product = nums.reduce((prev, curr) => curr? Math.imul(prev, curr): prev, 1);
    //     return nums.map(current => numberZeroes ? !current ? product : 0 : product / current);
    // }

    // Another way to implement without using divition
    // Calculate the prouct of all numbers left of nth number 
    // THEN calculate the right product AND multiply times current left product to obtain product of all nums to LEFT and RIGHT
    // Ex: nums: [1,2,3] prefix: [1, 1, 2]
    productExceptSelf(nums) {
        const result = [];
        let [prefix, postfix] = [1, 1];
        // Build the product of all the numbers to the indeces left
        for(let i = 0; i < nums.length; i++) {
            result[i] = prefix;
            prefix *= nums[i];
        }
        // Finish the products of all the numbers to the indeces right
        for(let i = nums.length - 2; i >= 0; i--) {
            postfix *= nums[i+1];
            result[i] *= postfix;
        }
        return result;
    }
}
