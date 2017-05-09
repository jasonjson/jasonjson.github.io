class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs.sort(key=len, reverse=True)
        for i, word1 in enumerate(strs):
            if all(not self.is_subseq(word1, word2) for j, word2 in enumerate(strs) if i != j):
                return len(word1)
        return -1

    def is_subseq(self, word1, word2):
        i = 0
        for char in word2:
            if i < len(word1) and word1[i] == char:
                i += 1
        return i == len(word1)
