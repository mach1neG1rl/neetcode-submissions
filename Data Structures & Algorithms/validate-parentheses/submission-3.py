class Solution:
    def isValid(self, s: str) -> bool:
        pair_map = {
            ")": "(", "}": "{", "]": "["
        }

        stack = []

        for i in s:
            if i in pair_map:
                if stack and stack[-1] == pair_map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False 