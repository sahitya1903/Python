class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertion(self, value):
        self.root = self.recursive_insertion(self.root, value)

    def recursive_insertion(self, root, value):
        if root is None:
            return Node(value)
        elif value < root.value:
            root.left = self.recursive_insertion(root.left, value)
        else:
            root.right = self.recursive_insertion(root.right, value)
        return root

    # Inorder: Left, Root, Right
    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.value, end=' ')
            self.inorderTraversal(root.right)

    # Preorder: Root, Left, Right
    def preorderTraversal(self, root):
        if root:
            print(root.value, end=' ')
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

    # Postorder: Left, Right, Root
    def postorderTraversal(self, root):
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            print(root.value, end=' ')

    def searching(self, root, value):
        if root is None:
            return False, None
        if root.value == value:
            return True, root
        if value < root.value:
            return self.searching(root.left, value)
        else:
            return self.searching(root.right, value)

    def min_node(self, root):
        while root.left:
            root = root.left
        return root

    def max_node(self, root):
        while root.right:
            root = root.right
        return root

    def delete(self, root, value):
        if root is None:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            # Case 1: Node has no children (leaf)
            if root.left is None and root.right is None:
                return None
            # Case 2: Node has one child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Case 3: Node has two children: find the inorder successor (min in right subtree)
            temp = self.min_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)
        return root

    def height(self, root):
        if root is None:
            return -1  # Height of empty tree is -1 (or 0, depending on convention)
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height, right_height)

    def isValidBST(self, node, min_val=float('-inf'), max_val=float('inf')):
        if node is None:
            return True
        if not (min_val < node.value < max_val):
            return False
        return (self.isValidBST(node.left, min_val, node.value) and 
                self.isValidBST(node.right, node.value, max_val))

# Let's test our Binary Search Tree with a series of insertions
bst = BinarySearchTree()
values = [8, 3, 10, 1, 6, 4, 7, 9, 14, 13, 16]

for val in values:
    bst.insertion(val)

print("Inorder Traversal (should be sorted):")
bst.inorderTraversal(bst.root)
print("\n")  # Newline for clarity

print("Preorder Traversal:")
bst.preorderTraversal(bst.root)
print("\n")

print("Postorder Traversal:")
bst.postorderTraversal(bst.root)
print("\n")

# Test searching
found, node = bst.searching(bst.root, 7)
print("Searching for 7:", "Found" if found else "Not Found")

# Test height of the BST
print("Height of BST:", bst.height(bst.root))

# Validate BST property
print("Is valid BST:", bst.isValidBST(bst.root))
