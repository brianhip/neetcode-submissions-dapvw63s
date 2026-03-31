class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    permute(nums) {
        const output =[];
        const helper = (subset = []) => {
            if(subset.length === nums.length) return output.push([...subset]);
            nums.forEach(num => {
                // Avoid reusing the same number
                if(subset.includes(num)) return;
                subset.push(num);
                helper(subset);
                subset.pop();
            })
        }
        helper();
        return output;
    }
}
