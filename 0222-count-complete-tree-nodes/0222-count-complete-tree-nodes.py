# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Same iterative BFS can be used.
        if not root:
            return 0
        queue : list = deque([root])
        count : int = 1
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    count += 1
                    queue.append(node.left)
                if node.right:
                    count += 1
                    queue.append(node.right)
        return count