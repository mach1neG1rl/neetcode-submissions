class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        j = len(digits) - 1
        if digits[j] == 9:
            
            while digits[j] == 9 and j > 0:
                digits[j] = 0
                j -= 1
            
            if digits[j] == 9:
                digits.insert(0, 1)
                digits[j+1] = 0
            else:
                digits[j] += 1
        
        else:
            digits[len(digits) - 1] += 1

        return digits