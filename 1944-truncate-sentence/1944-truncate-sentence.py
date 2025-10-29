class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # Another free ahh question.
        slist : list = s.strip().split()
        return " ".join(slist[:k])