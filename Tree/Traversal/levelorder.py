# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        
        ans = []
        queue = deque([root])

        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                temp = queue.popleft()

                if temp.left != None: queue.append(temp.left)
                if temp.right != None: queue.append(temp.right)

                level.append(temp.val)
            ans.append(level)
        return ans

            
        