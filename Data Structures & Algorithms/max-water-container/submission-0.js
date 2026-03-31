class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let maxArea = 0;
        let left = 0;
        let right = heights.length-1;
        while(left < right) {
            const width = right - left;
            const height = Math.min(heights[left], heights[right]);
            const currentArea = width * height;
            maxArea = Math.max(currentArea, maxArea);
            
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }

        }

        return maxArea;
    }
}
