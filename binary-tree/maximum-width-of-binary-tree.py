# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append((root, 0))
        max_width = 0
        while q:
            _, first_idx = q[0]
            for _ in range(len(q)):
                node,idx = q.popleft()
                if node.left:
                    q.append((node.left,idx*2))
                if node.right:
                    q.append((node.right, idx*2+1))
            _,last_idx = q[-1] if q else (None, 0)
            max_width = max(max_width, last_idx - first_idx+1)
        return max_width

                
