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


def reverseOrder(root, k):

    current = root
    node_stack = []

    count = 0
    while True:

        if current:
            node_stack.append(current)
            current = current.right
        elif node_stack:
            node = node_stack.pop()
            count += 1
            if count == k:
                return node.value
            current = node.left
        else:
            break

    return None


tree = BinaryTreeNode(6)
tree.left = BinaryTreeNode(3)
tree.right = BinaryTreeNode(9)
tree.left.left = BinaryTreeNode(1)


inOrder(tree)
# 1
# 3
# 6
# 9

print(reverseOrder(tree, 5))
