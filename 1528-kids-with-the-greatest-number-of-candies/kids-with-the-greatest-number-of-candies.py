class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        s=[]
        for i in candies:
            if i+extraCandies>=max(candies):
                s.append(True)
            else:
                s.append(False)
        return s

S=Solution()
print(S.kidsWithCandies([2,3,5,1,3],3))
