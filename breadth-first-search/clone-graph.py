"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}

        def dfs(node):
            if node in clone:
                return clone[node]
            copy = Node(node.val)
            clone[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return None if not node else dfs(node)
        
