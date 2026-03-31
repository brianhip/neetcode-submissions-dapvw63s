class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a,b)=> a-b);
        const history = new Set();
        const output = [];
        const twoSum = (left, right, target) => {
            while(left < right) {
                const currentSum = nums[left] + nums[right];
                const serialized = `${-target}-${nums[left]}-${nums[right]}`;
                if(currentSum === target && !history.has(serialized)) {
                    output.push([-target, nums[left], nums[right]]);
                    history.add(serialized);
                    left++;
                    right--;
                } else if(currentSum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        for(let i = 0; i < nums.length - 2; i++){
            twoSum(i+1, nums.length -1, -nums[i]);
        }
        return output;
    }
}
