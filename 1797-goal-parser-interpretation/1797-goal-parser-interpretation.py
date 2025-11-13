class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        for idx,char in enumerate(command):
            if command[idx] == '(':
                if command[idx + 1] == ')':
                    ans.append('o')
                else:
                    continue
            elif char.isalpha():
                ans.append(char)
        return "".join(ans)