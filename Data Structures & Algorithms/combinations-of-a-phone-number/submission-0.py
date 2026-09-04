class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num_letters = [[] for i in range(10)]
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        current_number = 1
        for i in range(26):
            if 0 <= i <= 2:
                current_number = 2
            if 3 <= i <= 5:
                current_number = 3
            if 6 <= i <= 8:
                current_number = 4
            if 9 <= i <= 11:
                current_number = 5
            if 12 <= i <= 14:
                current_number = 6
            if 15 <= i <= 18:
                current_number = 7
            if 19 <= i <= 21:
                current_number = 8
            if 22 <= i <= 25:
                current_number = 9
            num_letters[current_number].append(alphabet[i])

        output = []
        def combinations(curr, index):
            if index == len(digits):
                curr_str = "".join(curr.copy())
                output.append(curr_str)
                return
            num_index = int(digits[index])
            for letter in num_letters[num_index]:
                curr.append(letter)
                combinations(curr, index + 1)
                curr.pop()
        combinations([], 0)
        return output