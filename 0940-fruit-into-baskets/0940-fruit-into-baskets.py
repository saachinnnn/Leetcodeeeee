class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxfruits = 0
        left = 0
        fruitcount = {}

        for right in range(len(fruits)):
            rightfruit = fruits[right]
            fruitcount[rightfruit] = fruitcount.get(rightfruit,0) + 1

            while len(fruitcount) > 2:
                leftfruit = fruits[left]
                fruitcount[leftfruit] -= 1
                if fruitcount[leftfruit] == 0:
                    del fruitcount[leftfruit]
                left += 1
            maxfruits = max(maxfruits,right - left + 1)
        return maxfruits

