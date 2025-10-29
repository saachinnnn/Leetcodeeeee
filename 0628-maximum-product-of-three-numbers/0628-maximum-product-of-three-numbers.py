class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # More like threesum(The name puhlease,idk abt the name gng)
        nums.sort()
        product_1 : int = nums[-1]*nums[-2]*nums[-3]
        product_2 : int = nums[-1]*nums[0]*nums[1]
        return max(product_1,product_2)