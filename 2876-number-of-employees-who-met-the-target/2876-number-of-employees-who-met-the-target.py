class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # Edge case.
        if len(hours) is 0:
            return 0
        count : int = 0
        for employee in hours:
            if employee >= target:
                count += 1
        return count 