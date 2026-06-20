class Solution:
    def isPalindrome(self, s: str) -> bool:
        # collect all the letters into a list and lower case
        only_letters = self.normalize(s)
        left = 0
        right= len(only_letters) - 1
        while left < right:
            if only_letters[left] != only_letters[right]:
                return False
            left += 1
            right -= 1
        return True

    def normalize(self, s: str) -> List[str]:
        output = []
        for char in s:
            if char.isalnum():
                output.append(char.lower())
        return output