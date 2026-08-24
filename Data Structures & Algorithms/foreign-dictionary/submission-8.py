class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
            UMPIRE:
                Understand:
                    In: List of words sorrted in lexicographical order for this new language
                    Out:
                    Constraint:
                Match:
                    dependency graphs
                    if dependencies don't form a cycle this is a valid language
                    so a DAG would be able to output the topological sort order if we use DFS
                    Gather on post number the current index and then reverse it

                    to for the dependencies compare two adjacent string until you find the first index that won't match 
                    then you know that the character that showed up first is the one that is before in the lexicographical order
                Plan:
                    # build the graph (adjecency map)
                    Create a hashmap with:
                        Key: the letter 
                        Value: a set with the letters that this character depend on to show up first
                    Initialize the hashmap with all the characters in all the words
                    
                    iterate over the list of words and check against the next word to find the first differing character
                        Possible edge case is that they are empty or they match completely
                        if they match completely then ignore it
                
                    # run dfs on graph to get topological order from post lists
                    based on the hashmap
                    run complete_DFS 

                    complete_DFS will have:
                        a visited list that maps to unique characters
                        a loop that starts first on all the characters that are not dependent on other words
                        an explore function that visits all reachable characters 
                        start loop
                Implement:
                Review:
                Evaluate:
        """
        graph_letters = {}
        for word in words:
            for letter in word:
                if letter not in graph_letters:
                    graph_letters[letter] = set()
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            smaller_len = min(len(word1), len(word2))
            is_same = True
            for j in range(smaller_len):
                if word1[j] != word2[j]:
                    graph_letters[word1[j]].add(word2[j])
                    is_same = False
                    break
            if is_same and len(word1) > len(word2):
                return ""

        def explore(letter, stack):
            if letter in visited:
                return visited[letter]
            visited[letter] = True
            for neighbor in graph_letters[letter]:
                if explore(neighbor, stack):
                    return True
            visited[letter] = False
            stack.append(letter)
            return False

        visited = {}
        output = []
        for letter in graph_letters.keys():
            if letter not in visited:
                explore(letter, output)

        if len(output) != len(graph_letters):
            return ""

        return ''.join(output[::-1])














