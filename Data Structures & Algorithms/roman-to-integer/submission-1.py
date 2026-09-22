class Solution:
    def romanToInt(self, s: str) -> int:
        # I
        # II
        # III
        # IV
        # V
        # VI
        # VII
        # VIII
        # IX
        # X
        # XI
        # XII

        magnitude = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        curr_num = 1
        i = 0
        while i < len(s):
            not_last = i < len(s) - 1
            if i == 0:
                if not_last and magnitude[s[i]] < magnitude[s[i + 1]]:
                    curr_num = magnitude[s[i + 1]] - magnitude[s[i]] 
                    i += 1
                else:
                    curr_num = magnitude[s[i]]
            else:
                if not_last and magnitude[s[i]] < magnitude[s[i + 1]]:
                    curr_num += magnitude[s[i + 1]] - magnitude[s[i]] 
                    i += 1
                else:
                    curr_num += magnitude[s[i]]
            i += 1
        return curr_num


                