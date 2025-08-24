from typing import List
class NumArray:
  def __init__(self,nums : List[int]):
    self.nums = nums
    for i in range(1,len(self.nums)):
      self.nums[i] += self.nums[i - 1]
  def sumRange(self,left : int,right : int):
    if left - 1 >= 0:
      return self.nums[right] - self.nums[left - 1]
    else:
      return self.nums[right]