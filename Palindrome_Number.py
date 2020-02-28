import numpy as np

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # Negatives cannot be palindromes

        if x < 0:
            return False
        if x == 0:
            return True
        # Save x so that we can check whether it is a palindrome later.
        original_x = str(x)
        # Initialize a list to hold all remainders
        remainders = []

        while x != 0:
            remainder = x % 10
            remainders.append(remainder)
            x = int(np.floor(x / 10))

        # Turn remainders to list of strings
        remainders = map(str, remainders)

        # Keep as a string, so that we don't lose the leading zero
        backwards_x = ''.join(remainders)

        # Check if is palindrome
        if backwards_x == original_x:
            return True
        else:
            return False


sol = Solution()
print(sol.isPalindrome(121))