# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def dfs(node, par=None):
            if node:
                parent[node] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        # Step 2: BFS from target
        q = deque()
        visited = set()

        q.append((target, 0))  # (node, distance)
        visited.add(target)

        res = []

        while q:
            node, dist = q.popleft()

            if dist == k:
                res.append(node.val)
            elif dist < k:
                for neighbor in [node.left, node.right, parent[node]]:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, dist + 1))

        return res
        
