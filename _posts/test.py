import collections
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        if not people:
            return []

        people_map = collections.defaultdict(list)
        height, ret =[], []
        for i, (h, k) in enumerate(people):
            people_map[h].append([k, i])
            if h not in height:
                height.append(h)
        height.sort(reverse=True)
        __import__('pprint').pprint(height)
        __import__('pprint').pprint(people_map)
        for h in height:
            people_map[h].sort()
            for (k, i) in people_map[h]:
                ret.insert(k, people[i])
        return ret

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
