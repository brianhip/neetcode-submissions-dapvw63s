class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        // count and keep track of top k elements
        const mapp = new Map();
        nums.forEach(num=>{
            let count = 0
            if (mapp.has(num)) {
                count = mapp.get(num);
            }
            mapp.set(num, count+1);
        });
        let result = [];
        mapp.forEach((value, key) => {
            result.push([value, key]);
        });
        result.sort((a, b) => b[0]-a[0]);
        return result.reduce((prev, curr, i) => {
            if(i < k) {
                prev.push(curr[1]);
            }
            return prev;
        },[])
    }
}
