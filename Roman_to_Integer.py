### Leet Code # 13 Roman to Integer

'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = 0
        second = 0
        length = len(s)
        numList = []
        
        for i in s: 
            if (i == "M"):
                numList.append(1000)
            elif (i == "D"):
                numList.append(500)
            elif (i == "C"):
                numList.append(100)
            elif (i == "L"):
                numList.append(50)
            elif (i == "X"):
                numList.append(10)
            elif (i == "V"):
                numList.append(5)
            elif (i == "I"):
                numList.append(1)
        


        for i in numList:
            if i < numList[i-1]:
                num = num + I

        return(num)

solution = Solution()
result = solution.romanToInt("LVIII")

            
print(result)



