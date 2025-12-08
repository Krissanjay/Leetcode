class Solution(object):
    def countTriples(self, n):
        c = 0
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                for k in range(j, n + 1):
                    if (i * i) + (j * j) == ((k * k)):
                        c = c + 1
        if c==1:
            return 2
        else:
            return c*2

S = Solution()
print(S.countTriples(5))