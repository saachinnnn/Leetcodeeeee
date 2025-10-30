class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return ""
        difference : int = abs(ord('A') - ord('a'))
        stack : list = []
        for char in s:
            if stack and abs(ord(stack[-1]) - ord(char)) == difference:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)