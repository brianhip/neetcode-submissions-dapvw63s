class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        // Potentially keep track of the characters and their indeces
        const cache = new Map();
        let maxSubstringSize = 0;
        let substrStart = 0;
        for(let i = 0; i < s.length; i++) {
            // When a repeated character is found
            let currChar = s[i]
            if(cache.has(currChar)) {
                let lastSeenIndex = cache.get(currChar);
                if(lastSeenIndex >= substrStart) {
                    substrStart = lastSeenIndex + 1;
                }
            }
            cache.set(currChar, i);
            maxSubstringSize = Math.max(1+i-substrStart, maxSubstringSize)
        }
        return maxSubstringSize;

    }
}
