class Solution(object):
    def randam_picket(self, nums, k):
        if not nums or not k:
            return []

        ret = nums[0:k]
        for i, num in enumerate(nums):
            j = random.randint(0, i)
            if j < k:
                ret[i] = num
        return ret
