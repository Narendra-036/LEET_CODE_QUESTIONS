# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=0
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        
        
        def check(root,l):
            if l==None:
                self.ans=1
                return
            if root.right and root.right.val==l.val:
                check(root.right,l.next)
            if root.left and root.left.val==l.val:
                check(root.left,l.next)
            
            
            
        def dfs(root):
            if root==None:
                return
            if root.val==head.val:
                check(root,head.next)
            dfs(root.left)
            dfs(root.right)
            
            
            
            
        dfs(root)
        if self.ans==1:
            return True
            
            
        