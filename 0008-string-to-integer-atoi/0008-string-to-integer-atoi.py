class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # safer than strip() for leading whitespace only
        if not s:
            return 0

        number = ""
        sign_seen = False

        for idx, char in enumerate(s):
            if char in "+-" and not sign_seen and idx == 0:
                number += char
                sign_seen = True
            elif char.isdigit():
                number += char
            else:
                break

        if number in ("", "+", "-"):
            return 0

        num = int(number)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        return max(INT_MIN, min(INT_MAX, num))