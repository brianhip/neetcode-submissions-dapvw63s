class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const groups = new Map();
        const stringArray = strs.map((str) => str.split("").sort().join(""));
        for(let i=0; i<stringArray.length; i++){
            let strsGroup = [];
            if(groups.has(stringArray[i])){
                strsGroup = groups.get(stringArray[i]);
            }
            strsGroup.push(strs[i]);
            groups.set(stringArray[i], strsGroup);
        }
        let output = [];
        groups.forEach((value, key) => output.push(value));
        return output;
    }
}
