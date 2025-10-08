class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # I think we take the ordinate value of the characters.

        low , high = 0 , len(letters) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # Now...
            if ord(letters[mid]) <= ord(target):
                low = mid + 1
            else:
                high = mid - 1

        return letters[low % len(letters)]