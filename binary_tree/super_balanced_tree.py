from tree_node import BinaryTreeNode


def is_balanced(root):

    node_stack = []
    node_stack.append((root, 0))
    depths = []

    while len(node_stack):
        node = node_stack.pop()
        # Check if a leaf node
        # (ie does not have a left or right node)
        # else add whatever node are present to the stack
        if (not node[0].left) and (not node[0].right):
            depths.append(node[1])
            max_depth = max(depths)
            min_depth = min(depths)
            if (max_depth - min_depth) > 1:
                return False

        else:
            if node[0].left:
                node_stack.append((node[0].left, node[1] + 1))

            if node[0].right:
                node_stack.append((node[0].right, node[1] + 1))

    return True


tree = BinaryTreeNode(6)
tree.left = BinaryTreeNode(3)
tree.right = BinaryTreeNode(9)
tree.left.left = BinaryTreeNode(1)
tree.left.left.left = BinaryTreeNode(1)


print(is_balanced(tree))
