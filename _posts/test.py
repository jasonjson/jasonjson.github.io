import collections
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        if not M:
            return 0

        num = len(M)
        visited = [False] * num
        queue = collections.deque()

        visited[0] = True
        queue.append(0)
        ret = 0
        while queue:
            i = queue.popleft()
            for j in xrange(num):
                if M[i][j] == 1 and not visited[j] and i != j:
                    queue.append(j)
                    visited[j] = True
            if not queue:
                ret += 1
                for i in xrange(num):
                    if not visited[i]:
                        queue.append(i)
                        visited[i] = True
                        break
        return ret

if __name__ == "__main__":
    solution = Solution()
    solution.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])
