class Solution {
    /**
     * @param {number} n - a positive integer
     * @return {number} - a positive integer
     */
    reverseBits(n) {
        
        console.log(n.toString(2));
        const str = n.toString(2);
        const reversed = [...str.split('').reverse(),...Array(32 - str.length).fill('0')];

        // console.log(parseInt(reversed.join(''), 2));
        return parseInt(reversed.join(''), 2);
    }
}
