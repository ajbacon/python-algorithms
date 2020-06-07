import math
from tree_node import BinaryTreeNode


def valid_bst(root):

    stack = [(root, -math.inf, math.inf)]

    while True:

        current, lower, upper = stack.pop()

        if (current.value <= lower) or (current.value >= upper):
            return False

        if current.left:
            stack.append((current.left, lower, current.value))

        if current.right:
            stack.append((current.right, current.value, upper))

        if not stack:
            break

    return True


tree = BinaryTreeNode(6)
tree.left = BinaryTreeNode(3)
tree.right = BinaryTreeNode(9)
tree.left.left = BinaryTreeNode(1)
tree.left.right = BinaryTreeNode(7)
tree.right.left = BinaryTreeNode(7)
tree.right.right = BinaryTreeNode(10)

print(valid_bst(tree))
