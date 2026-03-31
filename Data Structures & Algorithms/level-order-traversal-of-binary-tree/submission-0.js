/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[][]}
     */
    levelOrder(root) {
        if(!root) return [];
        const output = [];
        const queue = new Queue();
        // console.log(queue.size())
        queue.enqueue([root, 0]);
        while(queue.size()) {
            const [node, index] = queue.dequeue();
            if(node.left) queue.enqueue([node.left, index+1]);
            if(node.right) queue.enqueue([node.right, index+1]);
            if(output[index]) {
                output[index].push(node.val);
            } else {
                output[index] = [node.val];
            }

        }
        return output;
    }
}
