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
        nums.reduce((prod, curr, i) => {
            result[i] = prod
            return prod *= curr
        }, 1);
        return result.reduceRight((prod, curr, i) => {
            prod[0] *= i<nums.length-1? nums[i+1] : 1;
            prod[1][i] = curr * prod[0];
            return prod;
        }, [1, Array(nums.length).fill(1)])[1];
    }
}
