class Solution {
    /**
     * @param {number} n
     * @return {number[]}
     */
    countBits(n) {
        return Array(n+1).fill(0).map(this.bits);
    }
    bits(_, n) {
        return n.toString(2).split('0').reduce((prev, curr) => prev += curr.length, 0);
    }
}
