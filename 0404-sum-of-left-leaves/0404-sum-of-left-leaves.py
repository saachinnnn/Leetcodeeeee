# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # We can use the same iterative BFS approach and 
        ## can add the values of the left child.
        if not root:
            return 0
        queue : list = deque([root])
        answer : int = 0
        while queue:
            node = queue.popleft()
            if node.left:
                if node.left.left == None and node.left.right == None:
                    answer += node.left.val
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return answer