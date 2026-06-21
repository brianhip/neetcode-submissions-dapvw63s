class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
            Understanding:
                I: string with uppercase letters and int k which can repleace characters
                O: Return the length of the longest substring which contains only one distinct character
            Match:
                similar to longest susbtring with no duplicates
            Plan:
                initiate max_length variable to hold the longest substring with one distinct char
                initiate a dictionary to store the count of characters (maybe use defaultdict)
                initiate a left and right pointers
                initiate a max_frequency to keep track of the most frequent character
                while right pointer is in s lenght
                    increase char count in dictionary
                    update max_frequency to max of current character count and max_frequency
                    intitiate a curr_length variable (right - left + 1) 
                    while curr_length - max_frequency (or max(char_count)) > k:
                        Move left pointer to next character and update dictionary
                        Decrease the current length
                    max_length should be the max of itself and the curr_length

            Implement:
            Review:
                character count dictionary
                Use a sliding window that either grows if substring is valid or moves to left if curr substring is not valid
                    Check if sliding window is valid
                        A window is valid is non dominant characters count are less than or equal to k
                return length of sliding window
            Evaluate
        '''
        char_count = defaultdict(int)
        left, right = 0, 0
        max_frequency = 0
        while right < len(s):
            char_count[s[right]] += 1
            max_frequency = max(max_frequency, char_count[s[right]])
            is_valid = ((right - left + 1) - max_frequency <= k)
            if not is_valid:
                char_count[s[left]] -= 1
                left += 1
            right += 1
        return right - left