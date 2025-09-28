class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Okay now I this using python3.

        if len(nums) <=2:
            return 0
        
        count = 0 
        # We have to reverse the array.
        nums.sort(reverse = True)

        for i in range(len(nums) - 2):
            # Now we will get to know if the triangle has largest perimeter or not...
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2] # Returning the perimeter.
        return 0