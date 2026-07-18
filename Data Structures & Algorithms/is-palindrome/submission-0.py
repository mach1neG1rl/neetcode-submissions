class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char.lower()

        right = len(clean_s) - 1
        left = 0

        while left <= right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        
        return True