# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same(s, t):
            if not s and not t:
                return True
            if not s or not t or s.val != t.val:
                return False
            return is_same(s.left, t.left) and is_same(s.right, t.right)
            
        if not subRoot:
            return True
        if not root:
            return False
        if is_same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
