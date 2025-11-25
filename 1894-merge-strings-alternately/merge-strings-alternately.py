class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged=[]
        for a,b in zip(word1,word2):
            merged.append(a)
            merged.append(b)
        return "".join(merged)+word1[len(word2):]+word2[len(word1):]
Solution().mergeAlternately("abcd","pq")
        