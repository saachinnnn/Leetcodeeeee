class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0:
            return []
        
        L , R = 0 , len(numbers) - 1
        
        while L < R:
            value  = numbers[L] + numbers[R]
            if value == target:
                return [L + 1,R + 1]
            elif value > target:
                R -= 1
            else:
                L += 1
        return []
