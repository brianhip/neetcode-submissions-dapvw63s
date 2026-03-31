class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("$")
            res.append(s)
        encoded_str = "".join(res)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            strs.append(s[i:j])
            i = j
        return strs

