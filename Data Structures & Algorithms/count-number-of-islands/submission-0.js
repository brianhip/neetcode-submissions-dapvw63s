class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid) {
        const depthFirst = (i, j) => {
            if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] == "0") return;
            grid[i][j] = "0";
            for(let offset of [[1, 0], [0, 1], [-1, 0], [0, -1]]) {
                depthFirst(i+offset[0], j+offset[1]);
            }
        }
        let countOfIslands = 0;
        for(let i = 0; i < grid.length; i++) {
            for(let j = 0; j < grid[i].length; j++) {
                if (grid[i][j] === '1') {
                    depthFirst(i, j);
                    countOfIslands++;
                }
            }
        }
        return countOfIslands;
    }
}
