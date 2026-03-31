class Solution {
    /**
     * @param {number[]} candidates
     * @param {number} target
     * @return {number[][]}
     */
    combinationSum2(candidates, target) {
        // Need a helper function to create all possible unique combinations that add to target number
        candidates.sort((a, b)=> a-b);
        const output = new Set();
        const helper = (i, combSum, combination) => {
            console.log(combination);
            if(combSum <= 0 || i == candidates.length) {
                console.log("Reached the base case");
                if(combSum == 0) {
                    console.log("The combination array=", combination)
                    // Create a key
                    const key = [...combination].join(",");
                    output.add(key);
                }
                return;
            }
            combination.push(candidates[i]);
            helper(i+1, combSum - candidates[i], combination);
            combination.pop();
            helper(i+1, combSum, combination);
        }
        helper(0, target, []);
        return Array.from(output).map((key) => key.split(","));
    }
}
