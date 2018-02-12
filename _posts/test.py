class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height:
            return 0

        container = [0] * len(height)
        max_height = ret = 0

        for i in range(len(height)):
            __import__('pdb').set_trace()
            container[i] = max_height
            max_height = max(max_height, height[i])

        max_height = 0
        for i in reversed(range(len(height))):
            container[i] = min(container[i], max_height)
            max_height = max(max_height, height[i])
            diff = container[i] - height[i]
            ret += diff if diff > 0 else 0

        return ret

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.trap([0]))
