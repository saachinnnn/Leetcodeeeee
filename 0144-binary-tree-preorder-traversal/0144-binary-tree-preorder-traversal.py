# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def Preorder(node,ans):
            if not node:
                return []
            ans.append(node.val)
            Preorder(node.left,ans)
            Preorder(node.right,ans)
            return ans
        return Preorder(root,[])
        
        