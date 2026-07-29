# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        result = []
        reverse = False
        while q:
            qlen= len(q)
            level = []
            for _ in range(qlen):
                node = q.popleft()
                if reverse:
                    level.insert(0,node.val)
                else:
                    level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if reverse == True:
                reverse = False
            else:
                reverse = True
            result.append(level)    
        return result