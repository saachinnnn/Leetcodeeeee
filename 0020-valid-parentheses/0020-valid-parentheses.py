class Solution:
    def isValid(self, s: str) -> bool:
        stack : list = []
        matching : dict = {')':'(','}':'{',']':'['}
        for char in s:
            if char in matching.values():
                stack.append(char)
            elif char in matching:
                if not stack or matching[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                return False
        return not stack