class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        const mapCharToIndex = new Map();
        let longest = 0;
        let start = 0;
        for(let i = 0; i < s.length; i++) {
            let char = s[i];
            if (mapCharToIndex.has(char)) {
                let oldIndex = mapCharToIndex.get(char);
                if (oldIndex >= start){
                    start = oldIndex + 1;
                } 
            }
            mapCharToIndex.set(char, i);
            longest = Math.max(longest, 1 + i - start);
        }
        return longest;
    }
}
