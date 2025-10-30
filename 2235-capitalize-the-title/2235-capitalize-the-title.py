class Solution:
    def capitalizeTitle(self, title: str) -> str:
        if not title:
            return ""
        stringlist : list = title.strip().split()
        for idx,word in enumerate(stringlist):
            if len(word) > 0 and len(word) < 3:
                stringlist[idx] = word.lower()
            else:
                stringlist[idx] = word.lower().capitalize()
        return " ".join(stringlist)