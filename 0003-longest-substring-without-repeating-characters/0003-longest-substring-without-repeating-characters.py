class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        list_seen=[-1]*256
        l=r=0
        #n=len(s)
        max_len=0
        while r<n:
            if list_seen[ord(s[r])]!=-1:
                if list_seen[ord(s[r])]>=l:
                    l=list_seen[ord(s[r])]+1
            leng=r-l+1
            max_len=max(max_len,leng)
            list_seen[ord(s[r])]=r
            r+=1
        return max_len

        