class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Easy.
        stack : list = []
        for operation in operations:
            if operation == "+":
                val_1 = int(stack[-1])
                val_2 = int(stack[-2])
                stack.append(str(val_1 + val_2))
            elif operation == "D":
                stack.append(str(int(stack[-1])*2))
            elif operation == "C":
                stack.pop()
            else:
                stack.append(operation)
        return sum(int(num) for num in stack)