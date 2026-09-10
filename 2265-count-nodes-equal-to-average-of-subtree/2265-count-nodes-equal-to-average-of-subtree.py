# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        match_nodes=0
        def dfs(node):
            nonlocal match_nodes
            if node is None:
                return (0,0)
            #if node.left and node.right:
            left_sum,left_count=dfs(node.left)
            right_sum,right_count=dfs(node.right)
            tot_sum=node.val+left_sum+right_sum
            tot_count=1+left_count+right_count
            avg=tot_sum//tot_count
            if node.val==avg:
                match_nodes+=1
            return (tot_sum,tot_count)
        dfs(root)
        return match_nodes
        