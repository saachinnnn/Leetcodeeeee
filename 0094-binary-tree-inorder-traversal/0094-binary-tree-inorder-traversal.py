# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def Inorder(node,ans):
            if not node:
                return []
            Inorder(node.left,ans)
            ans.append(node.val)
            Inorder(node.right,ans)
            return ans
        ans : list = []
        ans = Inorder(root,ans)
        return ans
        