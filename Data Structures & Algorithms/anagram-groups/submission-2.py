from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            understanding: 
                Input: list of words
                Output: list of list of grouped anagrams from the original words
                Blackbox: We should create a function that checks if the words are anagrams and then group them together
            match:
                isAnagram function. 
                    Which we can solve in:
                        Using counters O(n + m) and O(1) space complexity
                        Sorting words in O(n log n) O(1)
                use a dictionary to group
            Plan:
                I believe if we use a counter a create a key from it we would have a unique key to use in our dictionary to group the words
                Create a dicitonary
                Iterate through the words
                    Create a unique key using a counter and convert into a string
                    Check if dictionary has it
                        yes -> add to the value which should be a list
                        no -> create an entrance add the unique key as key and add a list with the word as value
                return the values from the dictionary

            I:
            R:
            E: 
        '''
        word_groups = defaultdict(list)
        for word in strs:
            unique_key = self.createUniqueKey(word)
            word_groups[unique_key].append(word)
        return list( word_groups.values() )

    def createUniqueKey(self, word:str) -> str:
        alphabet_count = [0] * 26
        for character in word:
            alphabet_count[ord(character) - ord("a")] += 1
        return tuple(alphabet_count)

