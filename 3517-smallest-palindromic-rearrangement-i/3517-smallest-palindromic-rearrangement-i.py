class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        half=s[:len(s)//2]
        first_half="".join(sorted(half))
        if len(s)%2==0:
            middle_part=''
        else:
            middle_part=s[len(s)//2]
    
        return first_half+middle_part+first_half[::-1]