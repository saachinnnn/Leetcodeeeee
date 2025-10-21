class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for idx,char in enumerate(word):
            if char == ch:
                reverse_list = list(word[:idx + 1][::-1]) + list(word[idx + 1:])
                return "".join(reverse_list)
        return word