# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def BFS(node,ans):
            if not node:
                return []
            q : list = deque([node])
            while q:
                temp : list = []
                for _ in range(len(q)):
                    Node = q.popleft()
                    temp.append(Node.val)
                    if Node.left:
                        q.append(Node.left)
                    if Node.right:
                        q.append(Node.right)
                ans.append(temp)
            return ans
        return BFS(root,[])