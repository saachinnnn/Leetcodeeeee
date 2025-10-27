class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Simple logic,
        ## The wording was so confusing man.

        prev = 0
        lazer_count = 0

        for security_row in bank:
            curr = security_row.count('1')
            if curr:
                lazer_count += prev * curr
                prev = curr
        return lazer_count