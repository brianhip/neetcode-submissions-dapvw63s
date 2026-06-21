class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            UMPIRE:
                Understand:
                    Input:  string of charactes
                    Output: lenght of the longest substring without duplicate characters
                Match:
                    Dictionary that track last ocurrence of the character
                Plan:
                    Create a dictionary that we're going to use to store the visited charaters and it's last index
                    Have a start variable to track the starting point of the substring
                    Iterate from left to right the string
                        check if this char is in substring to see if it's a duplicate
                            HOW? the character is in the dictionary if so then check if the character occured within the substring check the index of last seen agains the start of substring
                            YES? Then update the starting to be old index of this letter plus 1 -> update new last index of current char
                        
                        calculate the substring lenght agains the max_substring lenght
                            HOW? max_length = max(max_length, current_index - start)
        """
        if len(s) == 0:
            return 0
        max_length = 0
        last_seen = {}
        start = 0
        for i in range(len(s)):
            char = s[i]
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            last_seen[char] = i
            max_length = max(max_length, i - start + 1)
        return max_length