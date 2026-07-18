class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_map = {}
        l = 0
        r = 0
        res = 0

        while r < len(s):
            
            if s[r] in str_map and str_map[s[r]]+1 > l: # b already in hashset, l = 2 
                l = str_map[s[r]]+1
            
            str_map[s[r]] = r # a: 0 b: 1 
            
            res = max(res, r-l+1) # 1: 1 , 2: 2, 3: l changes 1 4: 
            r += 1 # 0 1 2 3

        
        return res

                
