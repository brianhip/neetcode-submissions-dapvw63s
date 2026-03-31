class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        const cache = new Array(n+1).fill(-1);
        const helper = (steps = n) => {
            if (steps == 0) return 1;
            if (steps < 0) return 0;
            if (cache[steps] != -1) return cache[steps];
            cache[steps] = helper(steps - 1) + helper(steps - 2);
            return cache[steps];
        } 
        return helper(); 
    }
}
