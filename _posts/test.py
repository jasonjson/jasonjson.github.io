class Solution(object):
    def getSorted(self, nums, a, b, c):
        if not nums:
            return []

        if a == 0:
            ret = [b * num + c for num in nums]
            return ret if b > 0 else list(reversed(ret))

        mid = - b / (2.0 * a)
        left, right = [], []
        for num in nums:
            y = a * num * num + b * num + c
            if num < mid:
                left.append(y)
            else:
                right.append(y)
        ret = []
        if a > 0:
            i, j = len(left) - 1, 0
            while i >= 0 and j < len(right):
                if left[i] < right[j]:
                    ret.append(left[i])
                    i -= 1
                else:
                    ret.append(right[j])
                    j += 1
            while i >= 0:
                ret.append(left[i])
                i -= 1
            while j < len(right):
                ret.append(right[j])
                j += 1
        else:
            i, j = 0, len(right) - 1
            while i < len(left) and right >= 0:
                if left[i] < right[j]:
                    ret.append(left[i])
                    i += 1
                else:
                    ret.append(right[j])
                    j -= 1
            while i < len(left):
                ret.append(left[i])
                i += 1
            while j >= 0:
                ret.append(right[j])
                j -= 1
        return ret
