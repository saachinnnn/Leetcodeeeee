from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        if not students or not sandwiches:
            return 0
        
        q1 : list = deque(students)
        q2 : list = deque(sandwiches)
        count : int = 0
        while q1:
            if q1[0] == q2[0]:
                q1.popleft()
                q2.popleft()
                count = 0
            else:
                q1.append(q1.popleft())
                count += 1
            if count == len(q1):
                break
        return len(q1)