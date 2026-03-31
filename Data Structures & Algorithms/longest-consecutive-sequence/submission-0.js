class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const uniqueNums = new Set(nums);
        let maxLength = 0;
        nums.forEach(num => {
            if(!uniqueNums.has(num - 1)){
                let length = 1;
                while(uniqueNums.has(num + length)) {
                    length++;
                }
                maxLength = Math.max(length, maxLength);
            }
        })
        return maxLength;
    }
}
