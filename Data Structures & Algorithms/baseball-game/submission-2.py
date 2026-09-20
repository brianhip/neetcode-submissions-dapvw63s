class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack: list = []
        for i, operation in enumerate(operations):
            if operation == "+":
                stack.append(stack[-1] + stack[-2])
                continue
            if operation == "D" and len(stack):
                stack.append(stack[-1] * 2)
                continue
            if operation == "C" and len(stack):
                stack.pop()
                continue
            stack.append(int(operation))
        return sum(stack)