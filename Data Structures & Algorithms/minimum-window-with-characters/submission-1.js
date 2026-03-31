class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {
        const createCache = () => {
            let temp = new Map();
            t.split("").forEach(val => temp.set(val, (temp.get?.(val) || 0)+1));
            return temp;
        }
        let cacheTee = createCache();
        let shortSubstr = "";
        for(let left = 0; left <= s.length - t.length; left++) {
            if(cacheTee.has(s[left])) {
                for(let right = left; right < s.length; right++) {
                    if(cacheTee.has(s[right])) {
                        let count = cacheTee.get(s[right]);
                        if(count == 1) cacheTee.delete(s[right])
                        else cacheTee.set(s[right], count-1);
                    }
                    if(cacheTee.size==0) {
                        if(shortSubstr.length == 0 || shortSubstr.length>(right+1-left)) {
                            shortSubstr = s.substring(left, right+1);
                        }
                    }
                }
                cacheTee = createCache();
            }
        }
        return shortSubstr;
    }
}
