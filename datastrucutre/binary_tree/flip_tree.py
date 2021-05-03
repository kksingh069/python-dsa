class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def flip_tree(root):
    if root is None:
        return root

    if root.left is None and root.right is None:
        return root

    flipped_root = flip_tree(root.left)

    root.left.left = root.right
    root.left.right = root
    root.left = None
    root.right = None

    return flipped_root
