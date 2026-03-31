class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 10:40
        '''
            Understand:
                Input: string of character with possible duplicates
                Output: length of the the longest substring without duplicates
                    Substring: Is a contiguous sequence of characters within string
                Blackbox: Calculates the length of longest substring. 
                Constraints: 
            Match:
                Observations: 
                    We don't store the longest substring just its length
                    We want to track duplicates in a substring
                    We can use pointers start and end to know current substring
                    We save the last occurence of a character
                Build Test:
                Pattern:
                    Use a dictionary to store character as key and last index it occured as value
                    When the current character had ocurred before (is in dictionary) 
                    and the last occurence is in substring (dictionary[character] > start) 
                        then update start to be after last ocurrence and update the index in dictionary
            Plan: (pseudocode)
                initiate dictionary 
                initiate a variable max_length to hold the longest substring length
                initiate start and end pointers for substring
                while end pointer is within the substring
                    1. Get current character from the string
                    2. Check if current character is in dictionary
                        2.1. If currect chacter in dictionary check if it's last index is greater or equal to star
                            True -> update start to be last index + 1 
                        Update dictionary associated index for character to be end pointer
                    3. Else if not in dictionary
                        Add to dictionary
                    4. Calculate the max_length
                return max_length

            Implement: (actual code)
        '''
        last_char_index = {}
        max_length = 0

        start = 0
        end = 0
        while end < len(s):
            if s[end] in last_char_index and last_char_index[s[end]] >= start:
                start = last_char_index[s[end]] + 1

            last_char_index[s[end]] = end
            max_length = max(max_length, end - start + 1)
            end += 1

        return max_length        
        '''
            Review:
            Evaluate:
        '''