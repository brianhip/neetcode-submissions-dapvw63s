class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        // Reusable functions
        const width = ( L, R ) => R - L;
        const height = ( L, R ) => Math.min(heights[L], heights[R]);
        const currentArea = ( L, R ) => width(L, R) * height(L, R);
        // State
        let maxArea = 0;
        let left = 0;
        let right = heights.length-1;
        while(left < right) {
            maxArea = Math.max(currentArea(left, right), maxArea);
            heights[left] < heights[right] ? left++ : right--;
        }
        return maxArea;
    }
}
