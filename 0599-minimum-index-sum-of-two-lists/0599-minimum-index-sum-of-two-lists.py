class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {name: idx for idx, name in enumerate(list1)}
        MinimumCount = float('inf')
        answer = []
        for jdx, name in enumerate(list2):
            if name in index_map:
                index_sum = jdx + index_map[name]
                if index_sum < MinimumCount:
                    answer = [name]
                    MinimumCount = index_sum
                elif index_sum == MinimumCount:
                    answer.append(name)
        return answer