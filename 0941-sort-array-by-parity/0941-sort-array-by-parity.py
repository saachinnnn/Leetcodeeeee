class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Classic two pointer approach.
        ## This question is so nostalgic my god wow.

        if not nums:
            return []
        left_ptr : int = 0
        right_ptr : int = len(nums) - 1

        while left_ptr < right_ptr:
            if nums[left_ptr] % 2 != 0 and nums[right_ptr] % 2 == 0:
                nums[left_ptr] , nums[right_ptr] = nums[right_ptr] , nums[left_ptr]
                left_ptr += 1
                right_ptr -=1
            elif nums[left_ptr] % 2 == 0:
                left_ptr += 1
            else:
                right_ptr -= 1
        return nums