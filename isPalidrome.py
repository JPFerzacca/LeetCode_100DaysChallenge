class Solution(object):
    def isPalindrome(self, x):
        stringX = str(x)
        length = len(stringX)
        count = 0
        start = 0
        result = 0
        end = -1

        if (length % 2 == 0):
            mid = (length//2)-1
        else:
            mid = length//2
        if x >= 10:
            while count <= mid:
                if int(stringX[start]) != int(stringX[end]):
                    result = 0
                    break
                else:
                    count += 1
                    start +=1
                    end -= 1
                    result = 1           
        elif x >= 0:
            result = 1
        else:
            result = 0



        print(result)



solution = Solution()
result = solution.isPalindrome(1000021)


