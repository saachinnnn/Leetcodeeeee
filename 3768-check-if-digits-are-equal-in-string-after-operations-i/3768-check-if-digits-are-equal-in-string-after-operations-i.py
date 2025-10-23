class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Thinking of the most simple approach would be....
        # Edge case.
        if len(s) < 2:
            return False
        elif len(s) == 2:
            if s[0] == s[1]:
                return True
            else:
                return False
        while len(s) > 2:
            ans : list = []
            idx : int = 0
            while idx < len(s) - 1:
                ans.append(str((int(s[idx]) + int(s[idx + 1])) % 10))
                idx += 1
            newstring : str = "".join(ans)
            s = newstring
        return s[0] == s[1] if len(s) == 2 else False