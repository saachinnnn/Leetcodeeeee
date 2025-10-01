class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadanes doesnt work here.
        # We use the max_curr , min_curr and max_so_far strategy.

        max_curr : int = nums[0]
        min_curr : int = nums[0]

        max_so_far : int = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_curr , min_curr = min_curr , max_curr 
                # Swapping the roles apparently.
            max_curr = max(num,max_curr * num,)
            min_curr = min(num,min_curr * num)
            # Finally
            max_so_far = max(max_curr,max_so_far)
        return max_so_far
