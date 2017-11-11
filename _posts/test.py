class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        binary_data = map(self.to_binary_string, data)
        __import__('pdb').set_trace()
        index = 0
        while index < len(binary_data):
            first_char = binary_data[index]
            if first_char.startswith("0"):
                index += 1
            elif first_char.startswith("110"):
                if not self.verify(binary_data[index+1 : index+2]):
                    return False
                index += 2
            elif first_char.startswith("1110"):
                if not self.verify(binary_data[index+1 : index+3]):
                    return False
                index += 3
            elif first_char.startswith("11110"):
                if not self.verify(binary_data[index+1 : index+4]):
                    return False
                index += 4
        return True

    def verify(self, data):
        for d in data:
            if not d.startswith("10"):
                return False
        return True


    def to_binary_string(self, num):
        ret = []
        while num:
            ret.append(str(num % 2))
            num /= 2
        if len(ret) < 8:
            ret += ["0"] * (8 - len(ret))
        return "".join(reversed(ret))
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.validUtf8([237]))
