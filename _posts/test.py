import collections
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """

        if len(words1) != len(words2):
            return False

        word_map = collections.defaultdict(set)
        # for word in words1:
            # word_map[word].add(word)
        # for word in words2:
            # word_map[word].add(word)
        for a, b in pairs:
            word_map[a].add(b)
            word_map[b].add(a)

        for w1, w2 in zip(words1, words2):
            visited = set([w1])
            if not self.verify(w1, w2, word_map, visited):
                return False
        return True


    def verify(self, w1, w2, w_map, visited):
        if w1 == w2:
            return True
        for word in w_map[w1]:
            if word not in visited:
                visited.add(word)
                if self.verify(word, w2, w_map, visited):
                    return True
                visited.discard(word)
        return False

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.areSentencesSimilarTwo(["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]))
