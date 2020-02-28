import numpy as np
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # edge cases
        if x < 0 or (x % 10 == 0 and x != 0): 
            return False

        backwards_x = 0

        while backwards_x < x:
            backwards_x = backwards_x * 10 + (x % 10) # Build up the backwards number
            x //= 10

        # Check if is palindrome
        if backwards_x == x or backwards_x//10 == x:
            return True
        else:
            return False


sol = Solution()
print(sol.isPalindrome(10))