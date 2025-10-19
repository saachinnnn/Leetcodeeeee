class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Wait
        idx : int = len(digits) - 1
        while idx >= 0:
            if digits[idx] < 9:
                digits[idx] += 1
                return digits
            digits[idx] = 0
            if idx == 0:
                return [1] + digits
            idx -= 1
        return digits