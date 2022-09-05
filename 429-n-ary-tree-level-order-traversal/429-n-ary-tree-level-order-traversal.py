"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        
        q = deque([root]) if root else None
        while q:
            level = []
            len_ = len(q)
            for _ in range(len_):
                node = q.popleft()
                level.append(node.val)
                for child in node.children:
                    q.append(child)
            
            result.append(level)
            
        return result