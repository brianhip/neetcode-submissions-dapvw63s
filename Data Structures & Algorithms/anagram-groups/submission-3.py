from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            Understand:
                Input: a list of strings
                Output: Return a list of list with all the palindromes
        '''
        anagram_groups = {} # key: unique key - value: list_with_original words
        for word in strs:
            unique_key = self.createUniqueKey(word)
            if unique_key not in anagram_groups:
                anagram_groups[unique_key] = []
            anagram_groups[unique_key].append(word)
        output = []
        for key, list_with_original in anagram_groups.items():
            output.append(list_with_original)
        return output
        

    def createUniqueKey(self, word:str) -> str:
        # Create an array of size 26 to represent letter
        unique_count_letters = [ 0 for i in range(26)]
        # Count each letter appereance
        for char in word:
            unique_count_letters[ord(char)- ord("a")] += 1
        # return a string with that array with commas as delimiters
        return ",".join(map(str, unique_count_letters))