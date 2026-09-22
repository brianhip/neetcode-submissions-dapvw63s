class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = []
        carry = 1
        for digit in digits[::-1]:
            if digit == 9 and carry == 1:
                output.append(0)
                continue
            output.append(digit + carry)
            carry = 0
        if carry == 1:
            output.append(1)
        return output[::-1]
