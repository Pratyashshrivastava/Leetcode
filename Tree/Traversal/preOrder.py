class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
# Root->left->right
def preorder(root, arr):

    if not root:
        return
    
    arr.append(root.data)
    preorder(root.left, arr)
    preorder(root.right, arr)

def preOrder(root):
    arr = []

    preorder(root, arr)

    return arr

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    result = preOrder(root)

    print("preorder traversal: ", result)


    # preorder using stack iterative solution:
    # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        if not root:
            return
        
        stack = []

        stack.append(root)

        while len(stack) != 0:
            root = stack.pop()

            ans.append(root.val)

            if root.right is not None:
                stack.append(root.right)
            if root.left is not None: stack.append(root.left)

        return ans