class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def convert(root):
    if root is None:
        return 

    convert(root.left)
    convert(root.right)

    if root.left and root.right:
        root.val = root.left.val & root.right.val
