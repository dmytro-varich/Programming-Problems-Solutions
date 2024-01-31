# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                vertex = queue.popleft()
                if vertex:
                    count += 1
                    queue += [vertex.left]
                    queue += [vertex.right]
        return count 
