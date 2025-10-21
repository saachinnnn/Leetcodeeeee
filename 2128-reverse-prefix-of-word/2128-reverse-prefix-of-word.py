class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Using a stack.
        stack : list = []
        for idx,char in enumerate(word):
            if char == ch:
                stack.append(char)
                return "".join(stack[::-1] + list(word)[idx + 1:])
            else:
                stack.append(char)
        return word