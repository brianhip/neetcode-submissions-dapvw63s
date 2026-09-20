class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack: list = []
        for i, operation in enumerate(operations):
            if operation == "+":
                num_one = stack[-1]
                num_two = stack[-2]
                stack.append(num_one + num_two)
                continue
            if operation == "D" and len(stack):
                num_one = stack[-1]
                stack.append(num_one * 2)
                continue
            if operation == "C" and len(stack):
                stack.pop()
                continue
            stack.append(int(operation))
        print(stack)
        return sum(stack)