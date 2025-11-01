from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue : list = deque((idx,ticket) for idx,ticket in enumerate(tickets))
        secs : int = 0
        while queue:
            idx,ticket = queue.popleft()
            ticket -= 1
            secs += 1
            if ticket == 0 and idx == k:
                return secs
            elif ticket == 0 and idx != k:
                continue
            else:
                queue.append((idx,ticket))
        return secs