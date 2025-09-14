class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # Edge cases.
        if len(sentences) is 0:
            return 0
        maxlength : int = 0
        for sentence in sentences:
            maxlength = max(maxlength,len(sentence.split(" ")))
        return maxlength
