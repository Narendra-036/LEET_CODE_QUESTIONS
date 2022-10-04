# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traversal(node, currentSum):
            if not node: return False
            c = currentSum + node.val

            if node.left and node.right:
                return traversal(node.left, c) or traversal(node.right, c)
            elif node.left:
                return traversal(node.left, c)
            elif node.right:
                return traversal(node.right, c)
            else:
                return c == targetSum

        return traversal(root, 0)