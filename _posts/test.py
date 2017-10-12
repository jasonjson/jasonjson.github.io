#!/usr/bin/python

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        visited = [[False] * col for i in xrange(row)]
        ret = 0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == "1" and not visited[i][j]:
                    self.helper(grid, i, j, visited)
                    ret += 1
        return ret

    def helper(self, grid, i, j, visited):
        visited[i][j] = True
        if i - 1 >= 0 and grid[i - 1][j] == "1" and not visited[i - 1][j]:
            self.helper(grid, i - 1, j, visited)
        if i + 1 < len(grid) and grid[i + 1][j] == "1" and not visited[i + 1][j]:
            self.helper(grid, i + 1, j, visited)
        if j - 1 >= 0 and grid[i][j - 1] == "1" and not visited[i][j - 1]:
            self.helper(grid, i, j - 1, visited)
        if j + 1 < len(grid[0]) and grid[i][j + 1] == "1" and not visited[i][j + 1]:
            self.helper(grid, i, j + 1, visited)

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.numIslands(["11110","11010","11000","00000"]))
