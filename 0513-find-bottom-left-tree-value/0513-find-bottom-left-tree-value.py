# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q=[root]
        lef=[root.val]
        while q:
            for _ in range(len(q)):
                cur=q.pop(0)
                if cur.right:
                    q.append(cur.right)
                    lef.append(cur.right.val)
                if cur.left:
                    q.append(cur.left)
                    lef.append(cur.left.val)
        return lef[-1]