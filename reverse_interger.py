class Solution:
    def reverse(self, x: int) -> int:
        
        # As we loop through the bases, get the modulo at each
        modulo = 10
        digit = 1

        # Initialize a dict to hold the values
        digit_dict = {}
        # We get the remainder at the first one.
        remainder = x % modulo
        while remainder != x:
            
            digit_dict.update(
                {digit : remainder})
            modulo = modulo * 10
            digit += 1
            x = x - remainder
            remainder = int((x % modulo) / 10)

        return digit_dict
    
    # Now that we have the number of digits of
    # the number, loop backwards getting the modulo

sol = Solution()
print(sol.reverse(54567))