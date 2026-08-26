class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(o_count,c_count,curr_str):
            if len(curr_str)==2*n:
                res.append(curr_str)
                return
            if o_count<n:
                backtrack(o_count+1,c_count,curr_str+'(')
            if c_count<o_count:
                backtrack(o_count,c_count+1,curr_str+')') 
        backtrack(0,0,'')
        return res      