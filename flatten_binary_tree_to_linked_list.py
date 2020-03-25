class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        temp = TreeNode(0) 
        
        stack= [root]
        
        while stack:
            node = stack.pop()
            
            temp.right = node
            temp.left = None
            
            if node and node.right:
                stack.append(node.right)
                
            if node and node.left:
                stack.append(node.left)
                
            temp = node
        
        return temp

