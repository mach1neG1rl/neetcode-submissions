class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        mao = {}

        for i in s:
            if i not in mao:
                mao[i] = 1
            else:
                mao[i] += 1
        
        for j in t:
            if j not in s:
                return False
            mao[j] -= 1
        
        for key in mao:
            if mao[key] != 0:
                return False
        
        return True