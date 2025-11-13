class Solution:
    def interpret(self, command: str) -> str:
        # Using stack.
        stk = []
        for idx in range(len(command)):
            if command[idx] == '(':
                if command[idx + 1] == ')':
                    stk.append('o')
            elif command[idx].isalpha():
                stk.append(command[idx])
        return ''.join(stk)