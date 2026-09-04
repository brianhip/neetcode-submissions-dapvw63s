class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num_letters = [[] for i in range(10)]
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        current_number = 1
        for i in range(26):
            match i:
                case 0: current_number = 2
                case 3: current_number = 3
                case 6: current_number = 4
                case 9: current_number = 5
                case 12: current_number = 6
                case 15: current_number = 7
                case 19: current_number = 8
                case 22: current_number = 9
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