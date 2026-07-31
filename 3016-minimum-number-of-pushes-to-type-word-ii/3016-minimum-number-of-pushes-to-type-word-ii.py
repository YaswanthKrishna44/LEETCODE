from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq=Counter(word)
        freq_sorted=sorted(freq.values(),reverse=True)
        pushes=0
        for i,count in enumerate(freq_sorted):
            pushes_char=(i//8)+1
            pushes+=count*pushes_char
        return pushes



        