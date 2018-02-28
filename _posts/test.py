class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        if not input:
            return 0

        dir_list = input.split("\n")
        dir_map = {}
        ret = 0
        for directory in dir_list:
            level = directory.count("\t")
            name = directory[level:]
            if "." in directory:
                __import__('pdb').set_trace()
                size = len(name)
                for i in xrange(level):
                    size += len(dir_map[i]) + 1
                ret = max(ret, size)
            else:
                dir_map[level] = name
        return ret
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
