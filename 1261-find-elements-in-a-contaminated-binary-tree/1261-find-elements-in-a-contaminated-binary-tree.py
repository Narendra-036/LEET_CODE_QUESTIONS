# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root=root
        self.root.val=0
        q=[self.root]
        self.arr=[0]
        while q:
            for i in range(len(q)):
                cur=q.pop(0)
                if cur.left:
                    cur.left.val=2*cur.val+1
                    self.arr.append(cur.left.val)
                    q.append(cur.left)
                if cur.right:
                    cur.right.val=2*cur.val+2
                    self.arr.append(cur.right.val)
                    q.append(cur.right)
        

    def find(self, target: int) -> bool:
#         q=[self.root]
#         if self.root.val==target:
#             return True
#         while q:
#             for i in range(len(q)):
#                 cur=q.pop(0)
                
#                 if cur.left:
#                     if cur.left.val==target:
#                         return True
#                     q.append(cur.left)
#                 if cur.right:
#                     if cur.right.val==target:
#                         return True
#                     q.append(cur.right)
#         return False
        if target in self.arr:
            return True
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)