

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def diagonal_print_util(root, d, diagonal_map):
    if root is None:
        return

    try:
        diagonal_map[d].append(root.val)
    except:
        diagonal_map[d] = [root.val]

    diagonal_print_util(root.left, d+1, diagonal_map)

    diagonal_print_util(root.right, d, diagonal_map)


def diagonal_print(root):
    diagonal_map = dict()

    diagonal_print_util(root, 0, diagonal_map)
    
    for i in diagonal_map:
        for j in diagonal_map[i]:
            print(j, end=" ")
        print('')
