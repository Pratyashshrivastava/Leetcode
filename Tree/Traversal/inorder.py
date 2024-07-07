class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Left->Root->Right
def Inorder(root, arr):
    
    # base case:
    if root is None:
        return
    
    Inorder(root.left, arr)
    arr.append(root.data)
    Inorder(root.right, arr)

def in_order(root):
    arr = []

    Inorder(root,arr)

    return arr

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    result = in_order(root)

    print(result)