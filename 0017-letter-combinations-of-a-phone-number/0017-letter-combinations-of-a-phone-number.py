class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        phone_map={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def func(comb,next_digits):
            if len(next_digits)==0:
                output.append(comb)
            else:
                for letter in phone_map[next_digits[0]]:
                    func(comb+letter,next_digits[1:])
        output=[]
        func('',digits)
        return output
        