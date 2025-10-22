class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # Brute force.

        if not arr1 or not arr2:
            return 0
        
        seenset = set()
        anscount = 0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) not in seenset:
                    if abs(arr1[i] - arr2[j]) <= d:
                        break
                    seenset.add(abs(arr1[i] - arr2[j]))
            else:
                anscount += 1
        return anscount