class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    maxAreaOfIsland(grid) {
        const height = grid.length;
        const width = grid[0].length;
        const depthFirst = (i, j) => {
            if (i < 0 || j < 0 || i >= height || j >= width || !grid[i][j]) return 0;
            grid[i][j] = 0;
            let sum = 1;
            for(let offset of [[1,0],[0,1],[-1,0],[0,-1]]) {
                sum += depthFirst(i + offset[0], j + offset[1]);
            }
            return sum;
        }

        let maxArea = 0;
        for (let i = 0; i < height; i++) {
            for (let j = 0; j < width; j++) {
                maxArea = Math.max(maxArea, depthFirst(i, j));
            }
        }
        return maxArea;
    }
}
