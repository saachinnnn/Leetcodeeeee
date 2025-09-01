# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # BreadthFirstSearch.
        queue : list = deque([(root.left,root.right)])
        while queue:
            leftnode,rightnode = queue.popleft()
            if not leftnode and not rightnode:
                continue
            if not leftnode or not rightnode:
                return False
            if leftnode.val != rightnode.val:
                return False
            else:
                queue.append((leftnode.left,rightnode.right))
                queue.append((leftnode.right,rightnode.left))
        return True
