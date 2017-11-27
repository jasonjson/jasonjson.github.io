import random
class Solution(object):
    def pickRandom(self, root):
        if not root:
            return

        stack, ret = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                ret.append(root)
                root = root.right
        return ret[random.randInt(0, len(ret) - 1)]
