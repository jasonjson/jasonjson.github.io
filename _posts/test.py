class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return False

        size = len(board)
        for i in xrange(size):
            nums1, nums2 = [], []
            for j in xrange(size):
                if board[i][j] != "." and board[i][j] in nums[1]:
                    return False
                if board[j][i] != "." and board[j][i] in nums[2]:
                    return False
                nums1.append(board[i][j])
                nums2.append(board[j][i])
        for i in xrange(0, size, 3):
            for j in xrange(0, size, 3):
                nums3 = []
                for k in xrange(i, i + 3):
                    for l in xrange(j, j + 3):
                        if board[k][l] != "." and board[k][l] in nums3:
                            return False
                        nums3.append(board[k][l])
        return True
