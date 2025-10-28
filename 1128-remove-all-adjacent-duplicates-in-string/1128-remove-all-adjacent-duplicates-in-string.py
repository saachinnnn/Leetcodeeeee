class Solution:
    def removeDuplicates(self, s: str) -> str:
        # My code logic that i earlier made. Not bad but yeah not the best.
        if not s:
            return ""
        stack : list = []
        for character in s:
            stack.append(character)
            if len(stack) > 1 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        return "".join(stack)