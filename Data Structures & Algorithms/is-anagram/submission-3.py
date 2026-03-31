class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = collections.Counter(list(s))
        counter_t = collections.Counter(list(t))

        return counter_s == counter_t