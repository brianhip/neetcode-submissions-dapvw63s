class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let counter = (a) => {
            let mappi = new Map();
            for(let char of a){
                let count = 1;
                if(mappi.has(char)){
                    count = mappi.get(char) + 1;
                }
                mappi.set(char, count)
            }
            return mappi;
        }
        let sMap = counter(s)
        let tMap = counter(t);
        for(let [key, count] of sMap){
            console.log(count, tMap.get(key))
            if(count !== tMap.get(key)){
                return false;
            }
            tMap.delete(key);
        }
        return tMap.size == 0;
    }
}
