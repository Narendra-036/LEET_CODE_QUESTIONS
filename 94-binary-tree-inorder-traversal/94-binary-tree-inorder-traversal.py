# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        node = root
        S = []
        while node or S:
            if node:
                S.append(node)
                node = node.left
            else:
                node = S.pop()
                ans.append(node.val)
                node = node.right
        return ans