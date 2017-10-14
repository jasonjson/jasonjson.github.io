#!/usr/bin/python

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        degree_list = [0] * numCourses
        pre_list = [[] for i in xrange(numCourses)]
        for x, y in prerequisites:
            degree_list[x] += 1
            pre_list[y].append(x)
        stack = [index for index, i in enumerate(degree_list) if i == 0]
        while stack:
            curr = stack.pop()
            numCourses -= 1
            for j in pre_list[curr]:
                degree_list[j] -= 1
                if degree_list[j] == 0:
                    stack.append(j)
        return numCourses == 0
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.canFinish(2, [[0, 1]]))
