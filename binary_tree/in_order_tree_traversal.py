from tree_node import BinaryTreeNode


def inOrder(root):

    current = root
    node_stack = []

    while True:

        if current:
            node_stack.append(current)
            current = current.left
        elif node_stack:
            node = node_stack.pop()
            print(node.value)
            current = node.right
        else:
            break


tree = BinaryTreeNode(6)
tree.left = BinaryTreeNode(3)
tree.right = BinaryTreeNode(9)
tree.left.left = BinaryTreeNode(1)


inOrder(tree)

# 1
# 3
# 6
# 9
