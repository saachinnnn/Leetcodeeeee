class Solution:
    def makeGood(self, s: str) -> str:
        # I can solve this string quesiton.
        if not s:
            return ""
        stack : list = []
        for char in s:
            if stack and ((stack[-1] != char and stack[-1] == char.lower()) or (stack[-1] != char and stack[-1] == char.upper())):
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

