class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for str in strs:
            key=''.join(sorted(str))
            if key not in res:
                res[key]=[]
            res[key].append(str)
        return list(res.values())

        