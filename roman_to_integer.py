
class Solution:

    def romanToInt(self, s: str) -> int:
        # look up dict
        roman_dict = {"I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500, "M" : 1000}

        return_num = 0

        for i in range(0, len(s)- 1):
            
            if roman_dict[s[i]] < roman_dict[s[i + 1]] :
                return_num -= roman_dict[s[i]]
            else:
                return_num += roman_dict[s[i]]
        
        return return_num + roman_dict[s[-1]]

sol = Solution()
print(sol.romanToInt('XI'))