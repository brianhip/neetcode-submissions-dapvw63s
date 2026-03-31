class Solution {
    /**
     * @param {string[]} words
     * @returns {string}
     */
    foreignDictionary(words) {
        // Build a graph of adjecency relationships AND a map with each letter indegree number
        const adjecencyMap = new Map();
        const indegree = new Map();
        for(let word of words) {
            for(let char of word.split('')) {
                adjecencyMap.set(char, []);
                indegree.set(char, 0);
            }
        }
        for(let i = 0; i < words.length-1; i++) {
            let current = words[i];
            let next = words[i+1];
            if (next.length < current.length && current.startsWith(next)) {
                return "";
            }

            for(let char = 0; char < Math.min(next.length, current.length); char++) {
                if (current[char] != next[char]) {
                    const adjList = adjecencyMap.get(current[char])
                    const incomming = indegree.get(next[char]) + 1;
                    if (!adjList.includes(next[char])) {
                        adjList.push(next[char]);
                        indegree.set(next[char], incomming);
                    }
                    break;
                }
            }
        }
        // Build the queue to process the nodes in topological order and make sure to 
        const queue = new Queue();
        for(let [letter, incomming] of indegree) {
            if (!incomming) queue.enqueue(letter);
        }
        const orderedLetters = [];
        while(queue.size()) {
            const letter = queue.dequeue();
            orderedLetters.push(letter);
            for (let dependent of adjecencyMap.get(letter)) {
                // Update the dependent letters to decrease their incomming node because we just processed their upstream node!!!!!
                const incomming = indegree.get(dependent) - 1;
                indegree.set(dependent, incomming);
                if(!incomming) {
                    queue.enqueue(dependent);
                }
            }
        }
        if (orderedLetters.length !== indegree.size) {
            return "";
        }
        return orderedLetters.join("");
    }
}
