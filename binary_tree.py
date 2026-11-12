class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Binary Tree using PACADA
root = Node("P")
root.left = Node("A1")
root.right = Node("C")
root.left.left = Node("A2")
root.left.right = Node("D")
root.right.left = Node("A3")


# Display Binary Tree without traversal
def display_tree(node, level=0, position="Root"):
    if node is not None:
        print("   " * level + position + ": " + node.data)

        display_tree(node.left, level + 1, "Left")
        display_tree(node.right, level + 1, "Right")


# BFS Traversal
def bfs(root):
    if root is None:
        return

    queue = [root]

    while queue:
        current = queue.pop(0)
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


# DFS Traversal (Preorder)
def dfs(root):
    if root is None:
        return

    print(root.data, end=" ")
    dfs(root.left)
    dfs(root.right)
