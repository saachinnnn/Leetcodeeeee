class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')':'(','}':'{',']':'['}

        for ch in s:
            if ch in matching.values():
                stack.append(ch)
            elif ch in matching:
                if not stack or stack[-1] != matching[ch]:
                    return False
                stack.pop()
            else:
                return False
        return not stack