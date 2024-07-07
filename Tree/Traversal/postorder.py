class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# right->root->left

def postOrder(root, arr):

    if not root:
        return 
    
    postOrder(root.right, arr)
    arr.append(root.data)
    postOrder(root.left, arr)

def post_order(root):
    arr = []

    postOrder(root, arr)

    return arr

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    result = post_order(root)

    print(result)

