# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            return 1+max(left,right)
        def isBalance(root):
            if not root:
                return True
            return (isBalance(root.left) and isBalance(root.right) and 
                        abs(dfs(root.left) - dfs(root.right)) <= 1)
        return isBalance(root)