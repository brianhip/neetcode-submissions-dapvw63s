class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # use the first word as the longest common prefix and shorten it
        longest_common_prefix = list(strs[0])
        for word in strs:
            count_of_equal = 0
            for i, char in enumerate(longest_common_prefix):
                if i >= len(word):
                    break
                if char == word[i]:
                    count_of_equal += 1
                else:
                    break
            to_delete = len(longest_common_prefix) - count_of_equal
            while to_delete > 0:
                longest_common_prefix.pop()
                to_delete -= 1
        
        return "".join(longest_common_prefix)
