class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumOfSquares(num):
            sum = 0
            while num > 0:
                sum += (num % 10)**2
                num //= 10
            return sum
        
        num_set = set()

        while n != 1:
            n = sumOfSquares(n)
            if n in num_set:
                return False
            num_set.add(n)
        
        return True 
