class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums) {
        // Try with two step or three steps return the greatest of them
        if(nums.length == 1) return nums[0];
        const cache = new Array(nums.length).fill(-1);
        const helper = (pos) => {
            if (nums.length <= pos) return 0;
            if (nums.length - 1 == pos) return nums[pos];
            if (cache[pos] != -1) return cache[pos];
            const oneSkip = helper(pos + 2);
            const twoSkips = helper(pos + 3);

            cache[pos] = nums[pos] + Math.max(oneSkip, twoSkips);
            return cache[pos];
        }
        return Math.max(helper(0), helper(1));
    }
}
