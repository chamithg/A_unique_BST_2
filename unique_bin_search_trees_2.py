
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def generateTrees(self, n: int):
        def build(start, end):
            if start > end:return [None]
            
            output = []
            for i in range ( start,end+1):
                left = build(start, i-1)
                right = build(i+1, end)
                for l in left:
                    for r in right:
                        root=TreeNode(i)
                        root.left = l
                        root.right = r
                        output.append(root)
                        
            return output            
            
            
        
        return build(1,n)


obj = Solution()

print(obj.generateTrees(3))