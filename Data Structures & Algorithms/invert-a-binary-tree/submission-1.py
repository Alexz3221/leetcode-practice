# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.invertTreeHelper(root)
        return root
    def invertTreeHelper(self, i: TreeNode):
        if i.left:
            self.invertTreeHelper(i.left)
        if i.right:
            self.invertTreeHelper(i.right)

        temp = i.left
        i.left = i.right
        i.right = temp
