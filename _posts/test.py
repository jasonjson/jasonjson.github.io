class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if not input:
            return 0

        path_list = input.split("\n")
        len_list = [0] * len(path_list)
        max_len = 0
        for path in path_list:
            level = path.count("\t")
            len_list[level] = len(path) - level
            curr_length = sum(len_list[:level + 1]) + level
            if "." in path and curr_length > max_len:
                max_len = curr_length
        return max_len
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
