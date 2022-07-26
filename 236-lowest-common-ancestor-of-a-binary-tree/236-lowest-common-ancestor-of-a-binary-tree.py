class Solution:

    def lowestCommonAncestor(self, root, p, q):
        stack = [root]

        parent = {root: None}

        while p not in parent or q not in parent:

            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set()

        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]
        return q