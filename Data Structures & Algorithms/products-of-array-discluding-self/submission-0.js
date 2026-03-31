class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let countZero = 0;
        const product = nums.reduce((prev, curr) => {
            if(curr == 0) {
                countZero += 1;
                return countZero > 1 ? 0 : prev;
            }
            return prev*curr;;
        }, 1);
        if (countZero > 1) {
            return new Array(nums.length).fill(0);
        }
        if (countZero === 1) {
            let zeroIndex = nums.indexOf(0);
            let output = new Array(nums.length).fill(0);
            output[zeroIndex] = product;
            return output;
        }
        return nums.map(num => product / num);
    }
}
