class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    missingNumber(nums) {
        let res = nums.length; // This is the total number
        for(let i = 0; i < nums.length; i++) {
            res += i - nums[i];
            console.log(i, nums[i], res);
        }
        return res;
    }
}
