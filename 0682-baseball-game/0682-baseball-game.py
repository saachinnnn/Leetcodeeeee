class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Easy.
        stack : list = []
        for operation in operations:
            if operation == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif operation == "D":
                stack.append((int(stack[-1])*2))
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))
        return sum(num for num in stack)