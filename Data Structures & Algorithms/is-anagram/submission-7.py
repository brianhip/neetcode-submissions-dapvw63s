
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = self.createCounter(s)
        count_t = self.createCounter(t)
        for char, count in count_s.items():
            if char not in count_t or count_t[char] != count:
                return False
            del count_t[char]
        return len(count_t) == 0
    def createCounter(self, s: str) -> dict:
        count_s = {}
        for char in s:
            if char not in count_s:
                count_s[char] = 0
            count_s[char] += 1
        return count_s