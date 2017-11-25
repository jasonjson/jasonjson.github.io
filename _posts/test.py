#!/usr/bin/python
# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1

        row, col = len(grid), len(grid[0])
        print row, col
        nums = [[0] * col for _ in xrange(row)]
        distance = [[0] * col for _ in xrange(row)]
        buildings = 0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] != 1:
                    continue
                buildings += 1
                visited = [[False] * col for _ in xrange(row)]
                queue = collections.deque()
                queue.append([i, j])
                dist = 0
                while queue:
                    for _ in xrange(len(queue)):
                        x, y = queue.popleft()
                        nums[x][y] += 1
                        distance[x][y] += dist
                        if x - 1 >= 0 and grid[x - 1][y] == 0 and not visited[x - 1][y]:
                            queue.append([x-1, y])
                            visited[x-1][y] = True
                        if x + 1 < row and grid[x + 1][y] == 0 and not visited[x + 1][y]:
                            queue.append([x+1, y])
                            visited[x+1][y] = True
                        if y - 1 >= 0 and grid[x][y - 1] == 0 and not visited[x][y - 1]:
                            queue.append([x, y - 1])
                            visited[x][y - 1] = True
                        if y + 1 < col and grid[x][y + 1] == 0 and not visited[x][y + 1]:
                            queue.append([x, y + 1])
                            visited[x][y + 1] = True
                    dist += 1
        ret = 2 * 31 - 1
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == 0 and nums[i][j] == buildings:
                    ret = min(ret, distance[i][j])
        return ret if ret != 2 ** 31 - 1 else -1

if __name__ == "__main__":
    solution= Solution()
    __import__('pprint').pprint(solution.shortestDistance([[1]]))
