class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        freq={}
        max_fruits=0
        left=0
        for right in range(len(fruits)):
            freq[fruits[right]]=freq.get(fruits[right],0)+1
            if len(freq)>2:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1
            if len(freq)<=2:
                max_fruits=max(max_fruits,right-left+1)
        return max_fruits

        