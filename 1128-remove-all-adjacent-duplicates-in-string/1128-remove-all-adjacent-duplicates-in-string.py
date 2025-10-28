class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return ""
        DuplicateRemover : list = []
        for character in s:
            if DuplicateRemover and character == DuplicateRemover[-1]:
                DuplicateRemover.pop()
            else:
                DuplicateRemover.append(character)
        return "".join(DuplicateRemover)

            