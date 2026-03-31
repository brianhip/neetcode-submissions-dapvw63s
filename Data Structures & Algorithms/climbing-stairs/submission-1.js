class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        const helper = (steps = n) => {
            if (steps == 0) return 1;
            if (steps < 0) return 0;
            return helper(steps - 1) + helper(steps - 2);
        } 
        return helper(); 
    }
}
