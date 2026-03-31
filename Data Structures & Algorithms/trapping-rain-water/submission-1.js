class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        // Calculate the maximum water from left to right
        const maxWaterLeft = Array(height.length).fill(0);
        let tallestWall = height[0];
        for(let i = 1; i < height.length; i++) {
            if(height[i] > tallestWall) {
                tallestWall = height[i]
            }
            maxWaterLeft[i] = tallestWall - height[i];
        }
        const maxWaterRight = Array(height.length).fill(0);
        tallestWall = height[height.length-1];
        for(let i = height.length-2; i >= 0; i--) {
             if(height[i] > tallestWall) {
                tallestWall = height[i]
            } 
            maxWaterRight[i] = tallestWall - height[i];
        }
        let output = 0;
        for(let i = 0; i < height.length; i++) {
            output+=Math.min(maxWaterLeft[i], maxWaterRight[i]);
        }
        return output;
    }
}
