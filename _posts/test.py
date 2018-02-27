class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if not nums:
            return []
        if a == 0:
            if b > 0:
                return [b * num + c for num in nums]
            else:
                return [b * num + c for num in reversed(nums)]

        mid_point = - b / (2 * a)
        left, right, ret = [], [], []
        for num in nums:
            if num <= mid_point:
                left.append(num)
            else:
                right.append(num)
        if a > 0:
            left_index = len(left) - 1
            right_index = 0
            while left_index >= 0 or right_index < len(right):
                left_value = a * left[left_index] * left[left_index] + b * left[left_index] + c if left_index >= 0 else 2 ** 31 - 1
                right_value = a * right[right_index] * right[right_index] + b * right[right_index] + c if right_index < len(right) else 2 ** 31 - 1
                __import__('pdb').set_trace()
                if left_value < right_value:
                    ret.append(left_value)
                    left_index -= 1
                else:
                    ret.append(right_value)
                    right_index += 1
        elif a < 0:
            left_indx = 0
            right_index = len(right) - 1
            while left_index < len(left) and right_index >= 0:
                left_value = a * left[left_index] * left[left_index] + b * left[left_index] + c
                right_value = a * right[right_index] * right[right_index] + b * right[right_index] + c
                if left_value < right_value:
                    ret.append(left_value)
                    left_index += 1
                else:
                    ret.append(right_value)
                    right_index -= 1
        return ret
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.sortTransformedArray([-97,-95,-82,-81,-76,-75,-74,-73,-72,-69,-68,-66,-64,-61,-56,-53,-51,-50,-47,-46,-43,-41,-39,-33,-30,-30,-29,-28,-27,-26,-25,-25,-23,-22,-18,-16,-16,-15,-9,-4,-2,-1,5,16,20,20,21,21,24,24,33,39,40,44,44,49,51,53,54,55,57,58,58,59,62,63,65,67,68,69,71,72,73,73,74,76,77,78,79,81,88,90,91,92,92,96,97], 31, 71, 96))
