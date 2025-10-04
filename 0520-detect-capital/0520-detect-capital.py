class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_up = word.isupper()
        all_low = word.islower()
        title_case = word[0].isupper() and word[1:].islower()

        return all_up or all_low or title_case