class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let leftArea = new Array(height.length).fill(0);
        let rightArea = new Array(height.length).fill(0);
        // left -> right
        let maxHeight = 0;
        for (let i = 0; i < height.length; i++) {
            if (height[i] < maxHeight) {
                leftArea[i] = maxHeight - height[i];
            } else {
                maxHeight = height[i];
            }
        }
        // right -> left
        maxHeight = 0;
        for (let i = height.length - 1; i >= 0; i--) {
            if (height[i] < maxHeight) {
                rightArea[i] = maxHeight - height[i];
            } else {
                maxHeight = height[i];
            }
        }
        let outputArea = 0
        for (let i = 0; i < height.length; i++) {
            outputArea += Math.min(leftArea[i], rightArea[i])
        }
        return outputArea;
    }
}
