class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums) {
        if (nums.length == 1) return nums[0];
        if (nums.length <= 3) return Math.max(...nums);
        // Check if tje size of the nums array is of one and return it
        const helper = (pos, cache = new Array(nums.length).fill(-1), startIsZero = (pos == 0)) => {

            if (nums.length <= pos) return 0;
            if (nums.length - 1 == pos) return startIsZero ? 0 : nums[pos];
            if (cache[pos] != -1) return cache[pos];

            const oneSkip = helper(pos + 2, cache, startIsZero);
            const twoSkips = helper(pos + 3, cache, startIsZero);

            cache[pos] = nums[pos] + Math.max(oneSkip, twoSkips);

            return cache[pos];
        }
        // Make the two calls starting at position 0 and 1 with the respective second value
        return Math.max(helper(0), helper(1), helper(2));
    }
}
